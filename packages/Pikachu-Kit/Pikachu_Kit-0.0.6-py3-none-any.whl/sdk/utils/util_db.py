#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC
@file: util_db.py
@time: 2023/6/19 21:33
@desc:
"""

from sdk.base.base_db import BaseDB


class DataBase(BaseDB):
    def __init__(self, host: str, port: int,
                 username: str, password: str, db: str):
        super(DataBase, self).__init__(host, port, username, password, db)

    def load_data_to_sql(self, data: dict):
        """

        :param data:
        :return:
        """

    def get_table_heads(self, table):
        """

        :param table:
        :return:
        """
        return [i[0] for i in self.execute_sql(
            "SHOW COLUMNS FROM {table};".format(table=table))]

    def get_condition(self, data: dict):
        """

        :param data:
        :return:
        """
        if data.get("condition") is not None:
            condition_dic = data["condition"]
            lis = []
            _lis = []
            for k, v in condition_dic.items():
                if not k.startswith("__"):
                    if isinstance(v, str):
                        li = "`{}`='{}'".format(k, v)
                        lis.append(li)
                    elif isinstance(v, int):
                        li = "`{}`={}".format(k, v)
                        lis.append(li)
                else:
                    if k.startswith("__in_"):
                        li = "`{}` in ({})".format(
                            k.replace("__in_", ""), ",".join([str(i) for i in v]))
                        lis.append(li)
                    elif k.startswith("__btn_"):
                        li = "`{}` between {} and {}".format(
                            k.replace("__btn_", ""), v[0], v[-1])
                        lis.append(li)
                    elif k.startswith("__group_"):
                        li = "group by `{}`".format(v)
                        _lis.append(li)
                    elif k.startswith("__order_"):
                        li = "order by `{}`".format(v)
                        _lis.append(li)
                    elif k.startswith("__desc_"):
                        if v == "+":
                            li = "desc"
                        else:
                            li = "asc"
                        _lis.append(li)
                    elif k.startswith("__offset_"):
                        li = "offset {}".format(v)
                        _lis.append(li)
                    elif k.startswith("__limit_"):
                        li = "limit {}".format(v)
                        _lis.append(li)
                    elif k.startswith("__like_"):
                        li = "`{}` like %{}%".format(k[7:], v)
                        _lis.append(li)
                condition = " and ".join(lis)

                condition += " {}".format(" ".join(_lis))
            condition = " where {}".format(condition)
        else:
            condition = ""

        return condition

    def get_table(self, data: dict):
        """

        :return:
        """
        if data.get("table") is not None:
            table = "`{}`".format(data["table"])
        else:
            raise ValueError("sql table is None")
        return table

    def select(self, data: dict):
        """

        :param data:
        :return:
        """
        self.create_cursor()
        sql = "select {select} from {table} {condition};"

        table = self.get_table(data)

        if data.get("select") is None:
            select = "*"
        else:
            select = "{}".format(
                ",".join(["`{}`".format(i) for i in data["select"]]))

        condition = self.get_condition(data)

        sql = sql.format(select=select, table=table, condition=condition)
        tables_lis = self.get_table_heads(table)
        result = self.execute_sql(sql)
        out_lis = []
        for args in result:
            res = dict(zip(tables_lis, args))
            out_lis.append(res)
        self.logger.info(out_lis)
        return out_lis

    def update(self, data: dict):
        """

        :param data:
        :return:
        """
        def _get_update(data: dict):
            lis = []
            for k, v in data.items():
                if not k.startswith("__"):
                    if isinstance(v, int):
                        li = "`{}`={}".format(k, v)
                    elif isinstance(v, str):
                        li = "`{}`='{}'".format(k, v)
                else:
                    if k.startswith("__+_"):
                        li = "`{}` + {}".format(k[3:], v)
                    elif k.startswith("__-_"):
                        li = "`{}` + {}".format(k[3:], v)
                lis.append(li)
            return ", ".join(lis)

        self.create_cursor()
        sql = "update {table} set {update} {condition};"

        table = self.get_table(data)

        if data.get("update") is None:
            raise ValueError("sql update is None")
        else:
            update = _get_update(data["update"])
        condition = self.get_condition(data)
        sql = sql.format(table=table, update=update, condition=condition)

        result = self.execute_sql(sql)
        return result

    def insert(self, data: dict):
        """

        :param data:
        :return:
        """
        self.create_cursor()
        result = 0
        table = self.get_table(data)
        for args in data["insert"]:
            sql = "insert into {table} set {kv};"
            lis = []
            for key, value in args.items():
                if isinstance(value, int):
                    lis.append("`{}`={}".format(key, value))
                elif isinstance(value, str):
                    lis.append("`{}`='{}'".format(key, value))
            kv = ", ".join(lis)
            sql = sql.format(table=table, kv=kv)
            res = self.execute_sql(sql)
            result += res
        return result

    def delete(self, data: dict):
        """

        :param data:
        :return:
        """
        self.create_cursor()
        sql = "delete from {table} {condition};"
        condition = self.get_condition(data)
        table = self.get_table(data)
        sql = sql.format(table=table, condition=condition)
        result = self.execute_sql(sql)
        return result

    def execute(self, sql):
        """
        自定义执行sql
        :param sql:
        :return:
        """


if __name__ == '__main__':
    db = DataBase(
        host="localhost",
        port=3306,
        username="root",
        password="123456",
        db="answer_platform"
    )
    # db.select({
    #     "table":"answer_users",
    #     "condition":{
    #         "__in_id":[6,10]
    #     }
    # })
    # db.update({
    #     "table": "answer_users",
    #     "update":{
    #         "username": "huahua",
    #         # "phone": "18845876049"
    #     },
    #     "condition":{
    #         "__in_id":[10,7,6,8,9],
    #         # "session":"930e4d94d11ca3b261b02765b8ba88da"
    #     }
    # })
    # db.insert({
    #     "table": "answer_users",
    #     "insert":[
    #         {
    #             "username": "dauis",
    #             "passwd": "1232312",
    #             "phone":"14494474659"
    #         },
    #         {
    #             "username": "3213123",
    #             "passwd": "2312344",
    #             "phone": "14464486445"
    #         }
    #     ]
    # })

    db.delete({
        "table": "answer_users",
        "condition": {
            "__in_id": [10, 7, 6, 8, 9],
            # "session":"930e4d94d11ca3b261b02765b8ba88da"
        }
    })
