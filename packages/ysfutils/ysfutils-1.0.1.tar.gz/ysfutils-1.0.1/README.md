# utils - 我常用的工具类

## 1. mongo

1. `MongoClient`类: 通过该类的`get_client()`获取连接;
2. `bulk_upsert`方法: 适用于**单节点部署**的MongoDB数据库的高性能`insert`或`update`操作;
3. `TimeObjectId`类: 通过该类的`generate()`生成基于时间的MongoDB的`ObjectId`, 入参格式为`YYYY-MM-DD`或者`YYYY-MM-DD HH:MM:SS`;

例子:

```python
import math
import os
from multiprocessing.pool import Pool

from mongo import MongoClient, bulk_upsert


class Dmo:
    @staticmethod
    def multiprocessing_insert():
        # 生成待处理的原始数据
        all_data = []
        for num in range(1, 10000):
            all_data.append({"_id": num, "name": "chenjp"})
        ori_data_count = len(all_data)

        # 将原始数据分成cpu核数-1块
        sub_list_len = int(math.ceil(len(all_data) / float(os.cpu_count())))
        chunks_data = [all_data[i:i + sub_list_len] for i in range(0, len(all_data), sub_list_len)]

        deal_data_pool = Pool(processes=os.cpu_count())
        multiprocessing_deal_data_results = []
        for sub_list in chunks_data:
            multiprocessing_deal_data_results.append(
                deal_data_pool.apply_async(Dmo.multiprocessing_data, args=(sub_list, "insert"))
            )
        deal_data_pool.close()
        deal_data_pool.join()

        # 合并各进程的处理结果、收集各进程错误信息
        data_count_list = []
        err_list = []
        for res in multiprocessing_deal_data_results:
            sub_process_result = res.get()
            if sub_process_result[1]:
                err_list.append(sub_process_result[1])
            data_count_list.extend([sub_process_result[0]])

        # 获取各进程处理的数量
        deal_count = 0
        for sub_data in data_count_list:
            deal_count += sub_data

        # 返回原始数据总量、处理的总量、err信息list
        return ori_data_count, deal_count, err_list

    @staticmethod
    def multiprocessing_data(data_list, opera_type):
        url = "mongodb://xxx:xxx@192.168.0.88:49102/?authSource=xxx&authMechanism=SCRAM-SHA-1"
        ca = "/Users/yingsf/.ssh/ca/mongo/gwola/ca.crt"
        client = "/Users/yingsf/.ssh/ca/mongo/gwola/gwola_client.pem"
        db_client = MongoClient(url, client_cert=client, ca_cert=ca).get_client()
        return bulk_upsert(db_client, "demo_bulk_test", data_list, opera_type)


if __name__ == "__main__":
    try:
        aa = Dmo.multiprocessing_insert()
        bb = 1
    except Exception as err:
        print(err)
```

---

## 2. list

1. `chunks_list`方法: 按指定条件将list分片, 可以按片数或长度进行分片;
2. `compare_dict_in_list`方法: 比较两个list中的dict是否相等(key相等);

---

## 3. dataframe

取消`pandas`的`dataframe`的科学计数法显示, 实际使用时先import该函数, 然后执行`pd.options.display.float_format=pdFloatFormat`即可取消df的科学计数法显示.

---

## 4. pid

操作磁盘上的pid文件

---

## 5. job

例子:

```python
import time

from job import JobUtils, BackgroundScheduler
from mongo import MongoClient

JOB_FOLDER = "/Users/yingsf/Mycode.localized/Github/utils/demo/jobs"
# 从顶级目录到job文件夹所在目录的"."格式字符串, 注意顶级目录取决于你运行时所在的位置, 所以这里的顶级目录是demo不是utils
JOB_PACKAGE_PREFIX = "demo.jobs"
ALL_JOBS = JobUtils.get_all_jobs_from_job_folder(JOB_FOLDER, JOB_PACKAGE_PREFIX)


def default_job():
    """ 添加指定文件夹下的所有job, 全部使用默认配置
    """
    scheduler = BackgroundScheduler().scheduler
    for job in ALL_JOBS:
        scheduler.add_job(job.method, **job.run_args)
    scheduler.start()
    while True:
        time.sleep(10)


def custom_parameters_job():
    """ 自定义scheduler参数和job参数
    """
    job_config = {
        "jobstores": "memory",
        "executors": "process",
        "timezone": "Asia/Harbin",
        "max_workers": 10,
        "coalesce": False,
        "max_instances": "20",
        "replace_existing": False,
        "misfire_grace_time": 60 * 2,
        "daemonic": False
    }
    scheduler = BackgroundScheduler(**job_config).scheduler
    for job in ALL_JOBS:
        # job2使用进程池执行, 覆盖默认线程池的参数
        if job.run_args["id"] == "job2_test":
            job.run_args["executor"] = "thread"
            job.run_args["misfire_grace_time"] = 60 * 10
            job.run_args["replace_existing"] = True
        scheduler.add_job(job.method, executor="thread", replace_existing=True, misfire_grace_time=60*10, **job.run_args)
    scheduler.start()
    while True:
        time.sleep(10)


def mongo_job():
    """ 使用MongoDB作为后端存储的job
    """
    url = "mongodb://xxx:xxx@192.168.0.88:49102/?authSource=xxx&authMechanism=SCRAM-SHA-1"
    ca = "/Users/yingsf/.ssh/ca/mongo/gwola/ca.crt"
    client = "/Users/yingsf/.ssh/ca/mongo/gwola/gwola_client.pem"
    db_client = MongoClient(url, client_cert=client, ca_cert=ca).get_client()
    scheduler = BackgroundScheduler(jobstores="mongo", database_name="warehouse", collection_name="job_demo_mongo_store", mongo_client=db_client).scheduler
    for job in ALL_JOBS:
        scheduler.add_job(job.method, executor="process", replace_existing=True, misfire_grace_time=60*10, **job.run_args)
    scheduler.start()
    while True:
        time.sleep(10)


if __name__ == "__main__":
    try:
        mongo_job()
    except Exception as err:
        print(err)
```

---

## 6. sqlites

支持`SQLCipher版本4`加密的sqlite数据库
