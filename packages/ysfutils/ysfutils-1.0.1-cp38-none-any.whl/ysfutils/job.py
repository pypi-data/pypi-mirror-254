import collections
import copy
import datetime
import os
import pickle
from pathlib import Path
from typing import Any

from apscheduler.jobstores.base import JobLookupError, ConflictingIdError
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.jobstores.mongodb import MongoDBJobStore as OriMongoDBJobStore
from apscheduler.schedulers.background import BackgroundScheduler as ApsBackgroundScheduler
from apscheduler.util import maybe_ref, datetime_to_utc_timestamp
from bson import Binary
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

TIME_FORMAT_STR = "%Y-%m-%d %H:%M:%S"


class BackgroundScheduler:
    def __init__(self, **job_config_args: Any):
        """ 初始化apscheduler的BackgroundScheduler实例

        Notes:
            job_config_args应包含以下参数(除replace_existing和misfire_grace_time以外全部为str类型), 如果不提供则使用默认值:
                1. jobstores: 后端存储类型, 包括memory和mongo两种值, 默认值为memory;
                2. database_name: 数据库名, 当后端存储类型选择mongo时需要提供此值;
                3. collection_name: 表(集合)名, 当后端存储类型选择mongo时需要提供此值;
                4. mongo_client: mongodb的连接实例, 当后端存储类型选择mongo时需要提供此值;
                5. executors: 执行器, 目前apscheduler支持的有AsyncIOExecutor、GeventExecutor、ThreadPoolExecutor、ProcessPoolExecutor、TornadoExecutor、TwistedExecutor
                   我常用的有thread、process两种值. 默认thread. I/O密集型推荐使用threadpool, CPU密集型推荐使用processpool;
                6. timezone: 时区信息, 默认值为Asia/Shanghai;
                7. max_workers: 线程或进程数, 默认值20;
                8. coalesce: 默认为true. 当某种原因导致某个job积攒了好几次没有运行, 该参数为True时, 下次这个job被submit给executor时只会执行1次, 也就是最后这次, 反之会执行5次;
                9. max_instances: 用于限制同时运行的任务实例数量, 默认为2. 它控制着同一个任务的多个实例是否可以同时执行;
                10. replace_existing: 是否替换已存在的作业定义, 默认为True;
                11. misfire_grace_time: 默认为None, 作业的宽限时间或容忍时间, 即作业错过触发时间后的容忍时间窗口, 单位为秒;
                12. daemonic: 默认为True, 表示调度器是一个守护线程, 在主线程结束时会自动退出

        Returns:
            scheduler: BackgroundScheduler实例

        """
        _scheduler_config = {
            "apscheduler.jobstores.default": MemoryJobStore(),
            "apscheduler.job_defaults.coalesce": "true",
            "apscheduler.job_defaults.max_instances": "2",
            "apscheduler.timezone": "Asia/Shanghai"
        }
        # 1. 获取配置参数
        _jobstores = job_config_args.get("jobstores", "memory")
        _db_name = job_config_args.get("database_name", "")
        _col_name = job_config_args.get("collection_name", "")
        _mongo_client = job_config_args.get("mongo_client", None)
        _executors = job_config_args.get("executors", "thread")
        _timezone = job_config_args.get("timezone", "Asia/Shanghai")
        _max_workers = str(job_config_args.get("max_workers")) if job_config_args.get("max_workers", None) else "20"
        _coalesce = "true" if job_config_args.get("coalesce", True) else "false"
        _max_instances = str(job_config_args.get("max_instances")) if job_config_args.get("max_instances", None) else "2"
        _daemonic = job_config_args.get("daemonic", True)

        # 2. 根据入参更新apscheduler配置
        # 后端存储
        if _jobstores == "mongo":
            _scheduler_config["apscheduler.jobstores.default"] = MongoDBJobStore(
                database=_db_name,
                collection=_col_name,
                client=_mongo_client
            )
        # 执行器
        if _executors == "thread":
            _scheduler_config["apscheduler.executors.default"] = {
                "class": "apscheduler.executors.pool:ThreadPoolExecutor",
                "max_workers": _max_workers
            }
            _scheduler_config["apscheduler.executors.process"] = {
                "type": "processpool",
                "max_workers": _max_workers
            }
        elif _executors == "process":
            _scheduler_config["apscheduler.executors.default"] = {
                "class": "apscheduler.executors.pool:ProcessPoolExecutor",
                "max_workers": _max_workers
            }
            _scheduler_config["apscheduler.executors.thread"] = {
                "type": "threadpool",
                "max_workers": _max_workers
            }
        # 时区
        _scheduler_config["apscheduler.timezone"] = _timezone
        # 其他配置
        _scheduler_config["apscheduler.job_defaults.coalesce"] = _coalesce
        _scheduler_config["apscheduler.job_defaults.max_instances"] = _max_instances
        # 3. 创建scheduler
        self.scheduler = ApsBackgroundScheduler(_scheduler_config)
        self.scheduler.daemonic = _daemonic
        self.replace_existing = job_config_args.get("replace_existing", True)
        self.misfire_grace_time = job_config_args.get("misfire_grace_time", None)


class JobUtils:
    @staticmethod
    def import_job_method(obj_name):
        """ 通过名字(含有点符号'.'的字符串或不含)import相应的对象.

        Notes:
            1. 传入没有'.'分隔的字符时, 等价于import x
            2. 传入有'.'分隔的字符时, 例如x.y.z, 则等价于from x.y import z
        """
        if not isinstance(obj_name, str):
            obj_name = obj_name.encode('utf-8')
        if obj_name.count('.') == 0:
            return __import__(obj_name, None, None)
        parts = obj_name.split('.')
        obj = __import__('.'.join(parts[:-1]), None, None, [parts[-1]], 0)
        try:
            return getattr(obj, parts[-1])
        except AttributeError:
            raise ImportError(f"No module obj_named {parts[-1]}")

    @staticmethod
    def job_time_allowed(begin_time, end_time):
        """ 判断job是否在允许的时段内

        Args:
            begin_time: 字符串, 格式为08:00
            end_time: 字符串, 格式为08:00

        """
        begin = datetime.datetime.strptime(str(datetime.datetime.now().date()) + f"{begin_time}", "%Y-%m-%d%H:%M")
        end = datetime.datetime.strptime(str(datetime.datetime.now().date()) + f"{end_time}", "%Y-%m-%d%H:%M")
        # 当前时间
        n_time = datetime.datetime.now()
        # 判断当前时间是否在范围时间内
        if begin < n_time < end:
            return True
        else:
            return False

    @staticmethod
    def generate_job_date(run_type, time_str=None):
        """ 根据run_type生成job的开始运行时间

        Args:
            run_type: 字符串, 具体内容见代码
            time_str: 时分秒, 格式为08:00:00

        """
        job_start_time = None
        if run_type == "next_day_time":
            """ 次日某时运行 """
            tomorrow_str = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d") + " " + time_str
            job_start_time = datetime.datetime.strptime(tomorrow_str, TIME_FORMAT_STR)
        if run_type == "next_hour":
            """ 下一个整点 """
            hour_stamp = datetime.datetime.now().replace(minute=0, second=0, microsecond=0).timestamp()
            hour_datetime = datetime.datetime.fromtimestamp(hour_stamp)
            job_start_time = hour_datetime + datetime.timedelta(hours=1)
        if run_type == "next_half_hour":
            """ 下一个半点 """
            now = datetime.datetime.now()
            hour_stamp = now.replace(minute=0, second=0, microsecond=0).timestamp()
            hour_datetime = datetime.datetime.fromtimestamp(hour_stamp)
            if now.minute < 30:
                job_start_time = hour_datetime + datetime.timedelta(minutes=30)
            else:
                job_start_time = hour_datetime + datetime.timedelta(hours=1)
        if run_type == "next_minute":
            """ 下分钟 """
            job_start_time = (datetime.datetime.now() + datetime.timedelta(minutes=1)).replace(second=0, microsecond=0)
        if run_type == "today_time":
            """ 今日某时运行 """
            today_str = (datetime.date.today()).strftime("%Y-%m-%d") + " " + time_str
            job_start_time = datetime.datetime.strptime(today_str, TIME_FORMAT_STR)
        return job_start_time

    @staticmethod
    def refresh_job_run_args(job_run_args: dict):
        """ 更新job_run_args中的next_run_time为datetime格式, 同时删除无用的参数

        Notes:
            job_run_args是符合apscheduler要求的一个dict(key的名字与apscheduler的要求保持一致), 内容解释如下:
                {
                    "id": "job的id, 命名要有意义",
                    "method": "该py文件内需要由job启动的函数",
                    "trigger": "触发器即调度逻辑, 每个作业都由自己的触发器来决定下次运行时间. 值为interval或cron",
                    "运行间隔例如在trigger为interval时, 该值可能为days, hours, minutes等": 整数类型的数值, 例如10,
                    "next_run_time": "下次运行时间即首次运行时间, 具体值参见generate_job_date()",
                    "executors": "执行器类型, 包括thread和process两种值. I/O密集型推荐使用thread, CPU密集型推荐使用process"
                }
            完整的示例如下:
                {
                    "id": "send_password_expire_msg",
                    "method": "job_start",
                    "trigger": "interval",
                    "days": 1,
                    "next_run_time": "next_day, 00:00:00",
                    "executors": "process"
                }

        Args:
            job_run_args: job_run_args["next_run_time"]值的格式为不含逗号的字符串"next_minute"或包含逗号的字符串"next_day, 20:00"

        Return:
            更新next_run_time以及删除无用参数后的job_run_args

        """
        copied_job_run_args = copy.deepcopy(job_run_args)
        job_next_run_time = copied_job_run_args["next_run_time"]
        # 字符串内由逗号分隔
        if "," in job_next_run_time:
            para_list = job_next_run_time.replace(" ", "").split(",")
            copied_job_run_args["next_run_time"] = JobUtils.generate_job_date(para_list[0], para_list[1])
        else:
            copied_job_run_args["next_run_time"] = JobUtils.generate_job_date(job_next_run_time)
        # 删除可能存在的无用字段
        if "method" in copied_job_run_args:
            copied_job_run_args.pop("method")
        if "executors" in copied_job_run_args:
            copied_job_run_args.pop("executors")
        return copied_job_run_args

    @staticmethod
    def get_all_py_file(job_folder: str):
        """ 获取job_folder文件夹下所有的py文件, 不包含__init__.py文件, 不搜索__pycache__目录.

        Args:
            job_folder: 路径

        Returns:
            all_py_file_path: list类型["不包含.py后缀的路径"......], 未找到的时候返回空list

        """
        all_py_file_path = []
        root_dir = Path(job_folder)
        dirs = [p for p in root_dir.rglob('*') if p.is_dir() and p.name != "__pycache__"]
        for py_dir in dirs:
            # 只生成文件名中.py前面的内容, 例如demo.py只获取demo
            all_py_file_path += [str(f).replace(".py", "") for f in py_dir.rglob("*.py") if f.name != "__init__.py"]
        return all_py_file_path

    @staticmethod
    def get_all_jobs_from_job_folder(job_folder: str, job_package_prefix: str):
        """ 获取指定文件夹下的符合条件的py文件中的job信息

        Notes:
            只有py文件包含以下名为apscheduler_job_info的dict时, 才会被导入, dict解释如下:
                apscheduler_job_info = {
                    "id": "job的id, 命名要有意义",
                    "method": "该py文件内需要由job启动的函数",
                    "trigger": "触发器即调度逻辑, 每个作业都由自己的触发器来决定下次运行时间. 值为interval或cron",
                    "运行间隔例如在trigger为interval时, 该值可能为days, hours, minutes等": 整数类型的数值, 例如10,
                    "next_run_time": "下次运行时间即首次运行时间, 具体值参见generate_job_date()",
                    "executors": "执行器类型, 包括thread和process两种值. I/O密集型推荐使用thread, CPU密集型推荐使用process"
                }
            完整的示例如下:
                apscheduler_job_info = {
                    "id": "send_password_expire_msg",
                    "method": "job_start",
                    "trigger": "interval",
                    "days": 1,
                    "next_run_time": "next_day, 00:00:00",
                    "executors": "process"
                }

        Args:
            job_folder: 路径
            job_package_prefix: 从顶级目录到job文件夹所在目录的"."格式字符串, 例如demo.users.job

        Returns:
            all_jobs: list类型或空[], list中的数据是命名元组, 内容为: [job(job1的处理函数, job1的运行参数dict)......]

        """
        all_jobs = []
        job_tuple = collections.namedtuple("job", ["method", "run_args"])
        all_py_file_path = JobUtils.get_all_py_file(job_folder)
        if all_py_file_path:
            for py_file in all_py_file_path:
                # 把job_package_prefix中的"."替换为对应操作系统的路径分隔符("/"或"\"等), 目的是为了在py文件的路径中查找是否包含job_package_prefix
                replace_job_package_prefix = job_package_prefix.replace(".", os.sep)
                job_path_index_in_str = py_file.find(replace_job_package_prefix)
                """
                再将操作系统的路径分隔符("/"或"\"等)替换为".", 然后截取job_path_index_in_str之后的字符串
                目的是通过import_job_method函数导入该py文件, 导入后方便查找该py文件内是否包含apscheduler_job_info字典
                """
                job_py_package = py_file[job_path_index_in_str:].replace(os.sep, ".")
                # 只对含有apscheduler_job_info字典的文件进行操作
                job_py_cls = JobUtils.import_job_method(job_py_package)
                if hasattr(job_py_cls, "apscheduler_job_info"):
                    # 1. 导入需要job执行的函数
                    job_info = job_py_cls.apscheduler_job_info
                    job_method_name = job_info["method"]
                    job_abs_method_name = job_py_package + "." + job_method_name
                    job_imported_method = JobUtils.import_job_method(job_abs_method_name)
                    # 2. 删除job信息中对于Job.refresh_job_run_args()无用的method参数
                    if "method" in job_info:
                        job_info.pop("method")
                    # 3. 处理job_info中的next_run_time
                    job_run_args = JobUtils.refresh_job_run_args(job_info)
                    all_jobs.append(job_tuple(job_imported_method, job_run_args))
        return all_jobs

    @staticmethod
    def job_info_list_to_namedtuple_list(job_info_list: list):
        """ 将普通的list转为namedtuple的list

        Args:
            job_info_list: [{}, {}......], list中的dict内容示例如下:
                {
                    "id": "sync_month_update_log",
                    "method": "butian_log.utils.log.update.job_start",
                    "trigger": "interval",
                    "minutes": 10,
                    "next_run_time": "next_minute"
                }

        """
        result = []
        job_tuple = collections.namedtuple("job", ["method", "run_args"])
        for job_info in job_info_list:
            result.append(job_tuple(job_info["method"], job_info))
        return result


class MongoDBJobStore(OriMongoDBJobStore):
    """ 重写MongoDBJobStore, 添加next_run_time的可读表示, 运行的是哪个函数, 首次运行时间, 最后一次运行时间等 """

    def __init__(self, database, collection, client=None, pickle_protocol=pickle.HIGHEST_PROTOCOL, **connect_args):
        super().__init__()
        self.pickle_protocol = pickle_protocol

        if not database:
            raise ValueError('The "database" parameter must not be empty')
        if not collection:
            raise ValueError('The "collection" parameter must not be empty')

        if client is not None:
            self.client = maybe_ref(client)
        else:
            connect_args.setdefault('w', 1)
            self.client = MongoClient(**connect_args)

        self.collection = self.client[collection]

    def add_job(self, job):
        try:
            self.collection.insert_one({
                '_id': job.id,
                'func': job.__getstate__()['func'],
                'trigger': str(job.__getstate__()['trigger']),
                'add_job_time': job.__getstate__()['trigger'].start_date.strftime(TIME_FORMAT_STR),
                'last_run_time': job.next_run_time.strftime(TIME_FORMAT_STR),
                'netx_run_time_readable': (job.next_run_time + datetime.timedelta(seconds=job.__getstate__()["trigger"].interval_length)).strftime(TIME_FORMAT_STR),
                'next_run_time': datetime_to_utc_timestamp(job.next_run_time),
                'job_state': Binary(pickle.dumps(job.__getstate__(), self.pickle_protocol))
            })
        except DuplicateKeyError:
            raise ConflictingIdError(job.id)

    def update_job(self, job):
        changes = {
            'add_job_time': job.__getstate__()['trigger'].start_date.strftime(TIME_FORMAT_STR),
            'last_run_time': (job.next_run_time - datetime.timedelta(seconds=job.__getstate__()["trigger"].interval_length)).strftime(TIME_FORMAT_STR),
            'netx_run_time_readable': job.next_run_time.strftime(TIME_FORMAT_STR),
            'next_run_time': datetime_to_utc_timestamp(job.next_run_time),
            'job_state': Binary(pickle.dumps(job.__getstate__(), self.pickle_protocol))
        }
        result = self.collection.update_one({'_id': job.id}, {'$set': changes})
        if result and result.matched_count == 0:
            raise JobLookupError(job.id)
