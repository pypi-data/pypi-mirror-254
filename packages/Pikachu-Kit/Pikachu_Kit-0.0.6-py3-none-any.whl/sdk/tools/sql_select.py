# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author  : v_jiaohaicheng@baidu.com
@des     :归档查询条件生成

"""

from sdk.temp.temp_supports import IsSolution


class Solution(IsSolution):
    """

    """

    def __init__(self, **kwargs):
        super(Solution, self).__init__()
        self.__dict__.update({k: v for k, v in [
                             i for i in locals().values() if isinstance(i, dict)][0].items()})

    def make_sql_select_task_kind(self, task_id):
        """

        """
        sql = "SELECT `collection_source` FROM `ct_collection_task` WHERE `id` = {}".format(
            task_id)
        print(sql)
        return sql

    def make_sql_select_page_answer(self, task_id):
        """

        :param task_id:
        :return:
        """
        sql = "SELECT `is_archive`  FROM `ct_collection_page_answer` WHERE `task_id` = {} AND `audit_stage` NOT IN (6) limit 1".format(
            task_id)
        print(sql)
        return sql

    def make_sql_select_map_table_name(self, task_id):
        """

        """
        sql = "SELECT `item_table_name`  FROM `ct_collection_item_table_mapping` WHERE `task_id` = {}".format(
            task_id)
        print(sql)
        return sql

    def make_sql_select_map_update_data(self, table_name, task_id):
        """

        """
        sql = "SELECT `url`,`id`,`task_id`,1 FROM `{}` WHERE `task_id`={} and `audit_stage` not in (4,6)".format(
            table_name, task_id)
        print(sql)
        return sql

    def process(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        task_id = kwargs["task_id"]
        table_name = kwargs["table_name"]
        self.make_sql_select_task_kind(task_id)
        self.make_sql_select_page_answer(task_id)
        self.make_sql_select_map_table_name(task_id)
        self.make_sql_select_map_update_data(table_name, task_id)


if __name__ == '__main__':
    task_id = "5622"
    table_name = "ct_collection_item_04"
    e = Solution()
    e.process(task_id=task_id, table_name=table_name)
