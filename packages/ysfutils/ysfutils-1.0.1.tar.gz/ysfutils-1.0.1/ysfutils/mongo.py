import binascii
import calendar
import datetime
import os
import struct
import sys
import threading
from random import SystemRandom
from typing import Any

from bson import ObjectId
from pymongo import InsertOne, UpdateOne
from pymongo import MongoClient as PyMongoClient
from pymongo.database import Database
from pymongo.errors import ConnectionFailure, OperationFailure, BulkWriteError


class MongoClient:
    """ 封装自己常用的2种连接MongoDB的方式 """

    def __init__(self, db_url: str, timeout: int = 10 * 1000, **kwargs: Any):
        """ MongoDB连接实例, 只接受mongodb://这样的连接方式, 不支持传统的host, port那种连接方式

        Args:
            db_url: 形如"mongodb://用户名:密码@地址:端口/?authSource=数据库名&authMechanism=SCRAM-SHA-1"
            client_cert: 开启tls时需要该参数, 客户端证书绝对路径
            ca_cert: 开启tls时需要该参数, ca证书绝对路径
            timeout: MongoClient连接的超时时间, MongoClient默认是30秒, ping的时候也会使用该时间，这里改成10秒

        Notes:
            db_url详细格式参考https://www.mongodb.com/docs/manual/reference/connection-string/

        Returns:
            MongoClient或抛出异常, 异常包括ConnectionFailure或OperationFailure

        """
        self.__mongo_url = db_url
        self.__timeout = timeout
        self.__db_name = db_url[db_url.find('?authSource=') + len('?authSource='):db_url.find('&authMechanism')]
        self.__ca_cert = kwargs.get("ca_cert", None)
        self.__client_cert = kwargs.get("client_cert", None)

    def get_client(self):
        """ 获取MongoClient """
        if self.__client_cert and self.__ca_cert:
            client = PyMongoClient(self.__mongo_url,
                                   tls=True,
                                   tlsAllowInvalidHostnames=False,
                                   tlsCertificateKeyFile=self.__client_cert,
                                   tlsAllowInvalidCertificates=False,
                                   tlsCAFile=self.__ca_cert,
                                   serverSelectionTimeoutMS=self.__timeout,
                                   connect=False)
        else:
            client = PyMongoClient(self.__mongo_url, serverSelectionTimeoutMS=self.__timeout, connect=False)
        try:
            db_client = client[self.__db_name]
            client.admin.command('ping')
        except ConnectionFailure:
            # ip和port问题时进入该异常
            _, exc_value, _ = sys.exc_info()
            raise ConnectionFailure(exc_value) from None
        except OperationFailure:
            # db和passwd问题时进入该异常
            _, exc_value, _ = sys.exc_info()
            raise OperationFailure(exc_value) from None
        return db_client


def bulk_upsert(db: Database, collection_name: str, docs: list[dict], opera_type: str = "insert"):
    """ 高性能批量向mongo插入或更新数据(适用于单节点部署的MongoDB数据库)

    Args:
        db: pymongo.MongoClient实例
        collection_name: 集合名
        docs: list类型, 要插入的批量文档, list的每个元素是dict[注意, 文档中必须有_id]
        opera_type: 操作类型, insert或update

    Notes:
        该方法不会raise异常, 主要是考虑使用multiprocessing.pool多进程调用时, 子进程出现异常可能会影响pool的正确性;
        同时, 该方法没有在事务中实现bulkWrite, 主要是考虑到MongoDB的版本和多进程问题;
        所以, 调用该方法时一定要比对该方法返回的数量与应该处理的正确数量, 如果数量不符则需要调用者进行异常处理, 例如回滚操作等;
        MongoDB的bulkWrite方法要求在更新或替换操作时, 只能根据_id的值进行操作, 即文档必须包含_id字段;
        当传入的文档中不包含_id字段时, 本方法并不会报错, 但返回值会提示0条被update, 原因参见第一条;
        因为我用的MongoDB都是单节点的, 所以只关注返回值中的writeErrors, 如果是集群的MongoDB, 还需要同时关注writeConcernErrors;
        由于ordered默认为true, 所以writeErrors的list实际上只包含一个dict, 后面的数据不会被操作;
        当ordered为false时, writeErrors的list包含array中的每个错误, 所以writeErrors的list包含多个dict, 后面的数据会继续被操作;

    Returns:
        返回(处理的数量, [信息]), 成功操作时, 第二个返回值为空list, 即[]. 失败时, 第二个参数为一个包含dict的list, 即[{错误信息}]

    """
    sucess_number, fail_number = 0, 0
    requests = []
    if (not docs) or (opera_type not in ["insert", "update"]):
        return fail_number, [{"writeErrors": "empty docs, or opera_type not 'insert'、'update'."}]
    # 生成批量request
    if opera_type == "insert":
        for i in docs:
            requests.append(InsertOne(i))
    if opera_type == "update":
        for i in docs:
            requests.append(UpdateOne({"_id": i.get("_id", None)}, {"$set": {**i}}))
    try:
        result = db[collection_name].bulk_write(requests)
        if opera_type == "insert":
            sucess_number = result.inserted_count
        elif opera_type == "update":
            sucess_number = result.matched_count
        return sucess_number, result.bulk_api_result["writeErrors"]
    except BulkWriteError as err:
        if opera_type == "insert":
            fail_number = err.details["nInserted"]
        elif opera_type == "update":
            fail_number = err.details["nMatched"]
        return fail_number, err.details["writeErrors"]


def _random_bytes() -> bytes:
    """ Get the 5-byte random field of an ObjectId. """
    return os.urandom(5)


class TimeObjectId:
    """ 根据时间字符串生成MongoDB的ObjectId """

    _MAX_COUNTER_VALUE = 0xFFFFFF

    _pid = os.getpid()

    _inc = SystemRandom().randint(0, _MAX_COUNTER_VALUE)
    _inc_lock = threading.Lock()

    # ObjectId的5字节随机bytes类型
    __random = _random_bytes()

    @classmethod
    def generate(cls, generation_time: str):
        """ 根据传入的时间生成MongoDB的ObjectId

        Args:
            generation_time: 格式为2023-01-01或者2023-01-01 00:01:02
        """
        # 时间为2023-01-01格式时, 补充后面的字符串
        try:
            date = datetime.datetime.strptime(generation_time, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            date_str = generation_time + ' ' + datetime.datetime.now().strftime('%H:%M:%S')
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

        # 1. 生成ObjectId中前4个bytes的时间
        offset = date.utcoffset()
        if offset is not None:
            date = date - offset
        timestamp = calendar.timegm(date.timetuple())
        oid = struct.pack(">I", int(timestamp))

        # 2. 5个bytes的随机数
        oid += TimeObjectId._random()

        # 3. 3个bytes的计数器
        with TimeObjectId._inc_lock:
            oid += struct.pack(">I", TimeObjectId._inc)[1:4]
            TimeObjectId._inc = (TimeObjectId._inc + 1) % (cls._MAX_COUNTER_VALUE + 1)

        return ObjectId(binascii.hexlify(oid).decode())

    @classmethod
    def _random(cls) -> bytes:
        """ 每个进程生成一次5个字节的随机数 """
        pid = os.getpid()
        if pid != cls._pid:
            cls._pid = pid
            cls.__random = _random_bytes()
        return cls.__random
