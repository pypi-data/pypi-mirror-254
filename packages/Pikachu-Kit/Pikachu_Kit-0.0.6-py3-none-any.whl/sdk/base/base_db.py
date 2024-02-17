#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC
@file: base_db.py
@time: 2023/6/19 21:34
@desc:
"""
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker,scoped_session
from contextlib import contextmanager
from sqlalchemy.pool import QueuePool
from sdk.base.base_tables import Base

class DB(object):
    """

    """
    def __init__(self,username,password,host,port,db,poll_size=50,debug=True):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.db = db
        self.poll_size = poll_size
        # 初始化数据库连接池:
        self.engine = create_engine(f'mysql+mysqlconnector'
                                    f'://{self.username}:{self.password}'
                                    f'@{self.host}:{self.port}/{self.db}',
                                    poolclass=QueuePool,pool_size=self.poll_size,echo=True if debug else False)
        self.__create_db()
        # 创建线程安全的DBSession类型:
        self.db_session = scoped_session(sessionmaker(bind=self.engine, autocommit=False))

    def __create_db(self):
        """
        新建表
        :return:
        """
        Base.metadata.create_all(self.engine, checkfirst=True)
    def run_origin_sql(self,session,sql):
        """
        执行原生sql
        :param session:
        :param sql:
        :return:
        """
        return session.execute(text(f"""{sql}"""))

    @contextmanager
    def get_session(self):
        """
        返回数据库连接对象
        :return:
        """
        session = self.db_session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
