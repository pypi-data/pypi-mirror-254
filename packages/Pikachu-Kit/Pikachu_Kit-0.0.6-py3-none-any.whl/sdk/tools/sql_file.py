# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author  : v_jiaohaicheng@baidu.com
@des     :归档数据格式化

"""

from sdk.temp.temp_supports import IsSolution
from sdk.utils.util_excel import ExcelProcess


class Solution(IsSolution):
    """

    """

    def __init__(self, **kwargs):
        super(Solution, self).__init__()
        self.__dict__.update({k: v for k, v in [
                             i for i in locals().values() if isinstance(i, dict)][0].items()})
        self.excel = ExcelProcess()

        self.his = "111"
        self.status = False

    def make_map_from_excel(self, file):
        """
        合格数据map
        :return:
        """
        map = {}
        for args in self.excel.read_yield(file):
            url = args["line"][args["headers"].index("url")]
            if map.get(url):
                print("重复:{}".format(url))
            else:
                map[url] = 1
        return map

    def make_map_from_excel2(self, file):
        map = {}
        for args in self.read_line(file):
            url = args["line"][args["headers"].index("bos地址")]
            if map.get(url):
                print("重复:{}".format(url))
            else:
                map[url] = 1
        return map

    def make_map_from_txt(self, file):
        map = {}
        for args in self.read_line(file):
            answer = self.get_answer(args, answer_list=["质检答案", "审核答案", "拟合答案"])
            # print(answer)
            url = args["line"][0]
            if answer == "合格":
                map[url] = 1
        return map

    def format_export(self, file):
        """
        格式化读取phpmyadmin导出的数据
        :param file:
        :return:
        """
        for args in self.read_line(file):
            data = args["line"]
            # print(data)
            if data == [''] and "== 转存表中的数据" in self.his:
                self.status = True
                continue

            if self.status:
                out = data[0].split("|")
                # print(out)
                yield out
            self.his = data[0]

    def process(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        in_path = kwargs["in_path"]
        save_path = kwargs["save_path"]

        self.folder.create_folder(save_path)

        file_export = self.folder.merge_path([in_path, "1.txt"])

        # file_excel = self.folder.merge_path([in_path, "1.xlsx"])
        # _stand_map = self.make_map_from_excel(file_excel)

        file_excel = self.folder.merge_path([in_path, "stand.txt"])
        # _stand_map = self.make_map_from_excel2(file_excel)
        _stand_map = self.make_map_from_txt(file_excel)

        # print(_stand_map)

        match_lis = []
        not_match_lis = []

        for _, url, id, task_id, status in self.format_export(file_export):
            if _stand_map.get(url) is None:
                print("匹配失败链接:{}".format(url))
                not_match_lis.append([id, task_id, "2"])
            else:
                match_lis.append([id, task_id, status])

        if match_lis:
            self.save_result(self.folder.merge_path(
                [save_path, "update_file.txt"]), data=match_lis)

        if not_match_lis:
            self.save_result(self.folder.merge_path(
                [save_path, "not_match.txt"]), data=not_match_lis)

    def process_export(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        in_path = kwargs["in_path"]
        save_path = kwargs["save_path"]

        self.folder.create_folder(save_path)

        file_export = self.folder.merge_path([in_path, "1.txt"])

        out_lis = []
        # for _, url, id, task_id, status in self.format_export(file_export):
        #     print(_, id, task_id, status)
        #     out_lis.append([id, task_id, status])

        for _, id, task_id, status in self.format_export(file_export):
            print(_, id, task_id, status)
            out_lis.append([id, task_id, status])

        self.save_result(self.folder.merge_path(
            [save_path, "update_file.txt"]), data=out_lis)

    def match_urls(self, file_export, file_stand):
        url_stand_set = set()
        for args in self.read_line(file_stand):
            # print(args)
            url = args["line"][args["headers"].index("question_value")]
            # answer_str = self.get_answer(args, answer_list=["审核答案", "质检答案","拟合答案"])
            # print(answer_str)
            url_stand_set.add(url)

        success_lis = []
        error_lis = []

        for args in self.read_line(file_export, spliter="|", headers=["_", "url", "id", "task_id"]):
            url = args["line"][args["headers"].index("url")]
            id = args["line"][args["headers"].index("id")]
            task_id = args["line"][args["headers"].index("task_id")]
            if url in url_stand_set:
                print("success")
                success_lis.append([id, task_id, "1"])
            else:
                print("error")
                error_lis.append([id, task_id, "2"])

        if success_lis:
            self.save_result(self.folder.merge_path(
                [save_path, "update_file.txt"]), data=success_lis)
        if error_lis:
            self.save_result(self.folder.merge_path(
                [save_path, "not_match.txt"]), data=error_lis)


if __name__ == '__main__':
    in_path = R"D:\Desktop\5"
    save_path = R"D:\Desktop\6"
    e = Solution()
    # 匹配url
    # e.process(in_path=in_path, save_path=save_path)

    # 直接导出数据处理
    e.process_export(in_path=in_path, save_path=save_path)

    # e.match_urls(R"D:\Desktop\5\export.txt", R"D:\Desktop\5\stand.txt")
