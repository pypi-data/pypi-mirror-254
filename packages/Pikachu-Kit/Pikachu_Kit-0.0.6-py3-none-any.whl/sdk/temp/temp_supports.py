#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC
@file: temp_supports.py
@time: 2023/6/20 21:57
@desc:
"""
import re
from sdk.utils import util_file, util_folder, util_json, util_encrtpt


class IsSolution(object):
    """

    """

    def __init__(self):

        self.file = util_file.FileProcess()
        self.folder = util_folder.FolderProcess()
        self.json = util_json.JsonProcess()
        self.encrypt = util_encrtpt.EncryptProcess()
        self.success_lis = []
        self.error_lis = []

    def get_file(self, folder: str, remove_list: list = [".DS_Store"], status=False):
        """

        :param folder:
        :return:
        """
        for args in self.folder.get_all_files(folder):
            file = args["file"]
            if args["name"] not in remove_list:
                if not status:
                    yield file
                else:
                    name = args["name"]
                    yield file, name

    def get_column(self, args: dict, key_lis: list) -> dict:
        """

        :param args:
        :param key_lis:
        :return:
        """
        headers = args["headers"]
        data = args["line"]
        num = args["num"]
        res = {}
        for key in key_lis:
            if headers.index(key) >= len(data):
                res[key] = ""
            else:
                res[key] = data[headers.index(key)]
        res["num"] = num
        return res

    def get_url_list(self, args):
        """

        :param args:
        :return:
        """
        url_str = args["line"][args["headers"].index("url")]
        try:
            url_list = self.json.loads(url_str)
        except BaseException:
            url_list = [url_str]
        return url_list

    def get_answer_list(self, args, answer_list, un_condition=["-", "是", "否", "{}", ""]):
        """

        :param args:
        :return:
        """
        answer_str = self.get_answer(args, answer_list=answer_list, un_condition=un_condition)
        if not answer_str.startswith("[answer error] "):
            answer_json = self.json.loads(answer_str)
            return answer_json["result"]
        else:
            raise ValueError("答案获取失败：{}".format(answer_str))

    def read_line(self, file: str, headers: list = None,
                  _id=False, spliter="\t", encoding="utf-8", mode="r"):
        """

        :param file:
        :param headers:
        :return:
        """
        for args in self.file.read_yield(
                file=file, headers=headers, spliter=spliter, encoding=encoding, mode=mode):
            if _id:
                id = args["line"][args["headers"].index("题目id")]
                if id == str(_id):
                    yield args
            else:
                yield args

    def read_line_col(self, file: str, header: list = None,
                      key_lis: list = None):
        """

        :param folder:
        :param header:
        :param key_lis:
        :return:
        """
        for args in self.file.read_yield(file=file, headers=header):
            data_json = self.get_column(args, key_lis)
            yield data_json

    def get_answer(self, args: dict, answer_list: list = [
                   "验收答案", "拟合答案", "质检答案"], un_condition: list = ["-", "是", "否", "{}", ""]):
        """
        取答案
        :param args:FileProcess返回的dict
        :param answer_list:取答案顺序
        :return:
        """
        num = args["num"]
        for key in answer_list:
            if key in args["headers"]:
                answer = args["line"][args["headers"].index(key)]
                if re.match(r'^\d+:{"', answer):
                    answer = ":".join(answer.split(":")[1:])
                if answer not in un_condition:
                    return answer
        return "[answer error] line num:{} answer:{}".format(num, answer)

    def parse_answer(self, answer, model="results"):
        """
        解析答案
        :param answer:
        :param model: results/elements/element
        :return:
        """
        if isinstance(answer, str):
            json_answer = self.json.loads(answer)
        else:
            json_answer = answer
        if json_answer.get("result"):
            result = json_answer["result"]
            if model == "results":
                yield result
                return
            else:
                for res in result:
                    if model == "elements":
                        yield res["elements"]
                        continue
                    else:
                        for element in res["elements"]:
                            if model == "element":
                                yield element
                                continue
        else:
            if model == "results":
                yield ["多帧数据，不存在result"]
                return
            else:
                if model == "elements":
                    yield json_answer["elements"]
                else:
                    for element in json_answer["elements"]:
                        if model == "element":
                            yield element
                            continue

    def get_points(self, points: dict, mode=0, format=False):
        """
        获取points
        :param points:
        :param mode:0:[[,],[,]] 2:[,,,,]
        :return:
        """
        try:
            if format:
                point_list = [[int(i["x"]), int(i["y"])] for i in points]
            else:
                point_list = [[i["x"], i["y"]] for i in points]
        except BaseException:
            pass

        if mode == 0:
            # 默认状况返回格式化后的数据
            # [[,],[,]]
            return point_list
        elif mode == -1:
            # 全展开 [,,,,,] 带x,y
            lis = []
            lis.extend(j for i in point_list for j in i)
            return lis
        elif mode == 2:
            # [[134, 409], [195, 468]] 全展开 [,,,,] 不带x,y
            return [j for i in points for j in i]

    def save_result(self, file: str, data, headers: list = None, mode="w"):
        """

        :param file:`
        :param data:
        :param headers:
        :return:
        """
        if len(file) > 260:
            raise ValueError("文件路径过长")
        with open(file, mode=mode, encoding="utf-8")as fp:
            if headers:
                fp.write("{}\n".format("\t".join(headers)))
            if isinstance(data, str):
                fp.write(data)
            if isinstance(data, list):
                for li in data:
                    if isinstance(li, list):
                        fp.write("{}\n".format("\t".join(li)))
                    else:
                        fp.write("{}\n".format(li))
            if isinstance(data, dict):
                fp.write(self.json.dumps(data))

            fp.flush()

    def make_out_path(self, base_path: str,
                      path_list: list = ["result"]) -> str:
        """
        生成输出路径
        :param base_path:根路径
        :param name:文件名
        :param path_list:根路径后拼接的路径列表
        :return:
        """
        # 拷贝个path_list副本操作
        _path_list = path_list[::]
        _path_list.insert(0, base_path)
        self.folder.create_folder(_path_list[0])
        _save_path = self.folder.merge_path(_path_list)
        self.folder.create_folder(_save_path)
        return _save_path

    def make_new_bos_url(self, uid, folder=None, name=None,
                         url=None, cut=4, folder_cut=3):
        """

        :param uid: 唯一标识
        :param folder:
        :param name:
        :param url:
        :param cut: 原始url保留长度
        :param folder_cut: 原始url保留层级（从后往前）
        :return:
        """
        if not name:
            name = self.folder.split_path(url)[-1]
        if not folder:
            folder = "/".join(self.folder.split_path(url)
                              [-(folder_cut + 1):-1])
        if not url:
            url = "https://bj.bcebos.com/collection-data/jiaohaicheng/{}/{}/{}".format(
                uid, folder, name)
        else:
            url = "/".join(self.folder.split_path(url)[:cut]) + "/{}/{}/{}".format(
                uid, folder, name
            )
        return url

    def process(self, **kwargs) -> str:
        """
        处理流程
        """
