import atexit
from contextlib import contextmanager, closing

from pysqlcipher3 import dbapi2 as sqlite3


class Sqlite3Client:
    """ sqlite3加密的封装

    Notes:
        1. 需要SQLCipher版本在4以上(我的版本是SQLCipher 4.5.4 community)
        2. execute和executemany在session环境下执行, 同一个session下全部执行成功则提交服务器, 执行中存在异常则全部回滚
        3. executescript会自动提交(所以不需要在session环境下执行). 建议只使用DDL语句并且自己写好COMMIT, 不建议用它插入或修改数据
        4. execute例子: execute('insert into test values(?,?,?)',[1,'Tom',23])
        5. executemany例子: executemany('insert into test values(?,?,?)',[[2,'Alice',22], [3,'John',21]])
        6. executescript例子: executescript('''
                                BEGIN;
                                CREATE TABLE person(firstname, lastname, age);
                                CREATE TABLE book(title, author, published);
                                CREATE TABLE publisher(name, address);
                                COMMIT;
                             ''')

    """
    def __init__(self, database: str, passwd: str = '', **kwargs):
        self.__passwd = str(passwd)
        kwargs['database'] = str(database)
        self.config = kwargs

    def __connect(self):
        if self.__passwd:
            conn = sqlite3.connect(**self.config)
            conn.execute(f'PRAGMA key={self.__passwd}')
        else:
            import sqlite3 as s3
            conn = s3.connect(**self.config)
        atexit.register(conn.close)
        return conn

    @contextmanager
    def session(self):
        conn = self.__connect()
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e

    def execute(self, sql: str, params=None):
        if params is None:
            params = []
        with self.session() as sl:
            return sl.execute(sql, params)

    def executemany(self, sql: str, params=None):
        if params is None:
            params = []
        with self.session() as sl:
            return sl.executemany(sql, params)

    def executescript(self, sql: str):
        return self.__connect().executescript(sql)

    def find(self, sql: str, params=None, multi=True):
        """ 执行sql语句, 返回多行或一行记录 """
        if params is None:
            params = []
        cur = self.execute(sql, params)
        with closing(cur):
            return cur.fetchall() if multi else cur.fetchone()
