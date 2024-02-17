# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: sort_2.py
@time: 2023/11/1 11:01
@desc: 统计 带data的dialog 10轮对话

"""

from sdk.temp.temp_supports import IsSolution


class Solution(IsSolution):
    def __init__(self, **kwargs):
        super(Solution, self).__init__()
        self.__dict__.update({k: v for k, v in [
            i for i in locals().values() if isinstance(i, dict)][0].items()})

    def sort_dict(self, dic):
        new_dic = {}
        for i in sorted([int(i) for i in dic.keys()]):
            v = dic.get(str(i))
            if isinstance(v, dict):
                v = self.sort_dict(v)
            new_dic[str(i)] = v
        return new_dic

    def sort_2(self, dic, name):
        col_map = {}
        lis = []
        for k, v in dic.items():
            if col_map.get(k) is None:
                col_map[k] = len(v)
            else:
                col_map[k] = col_map[k] + len(v)
            for k2, v2 in v.items():
                lis.append(self.json.loads(v2))
        print(name, col_map)
        return lis

    def process(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        in_path = kwargs["in_path"]
        save_path = kwargs["save_path"]
        self.folder.create_folder(save_path)
        for file, name in self.get_file(in_path, status=True):
            # print(file, name)
            map = {}
            repeat_lis = []
            no_dialog_lis = []
            for args in self.file.read_json_file(file):
                if args["data"]:
                    image = args["data"][0]["image"]
                    # print(image)
                    kind, key1, key2 = image.split(".")[0].split("/")[-1].split("-")
                    # print(kind,key1,key2)
                    dialog = args["data"][0]["dialog"]
                    if len(dialog) != 10:
                        # print("dialog 长度不合格：{} image {}".format(len(dialog),image))
                        no_dialog_lis.append([image, str(len(dialog))])

                    if map.get(key1) is None:
                        map[key1] = {
                            key2: self.json.dumps(args)
                        }
                    else:
                        if map[key1].get(key2) is None:
                            map[key1][key2] = self.json.dumps(args)
                        else:
                            # print("重复：{}".format(image))
                            repeat_lis.append([image])

            if repeat_lis:
                self.save_result(self.folder.merge_path([save_path, "{}_重复.txt".format(name)]), data=repeat_lis)
            if no_dialog_lis:
                self.save_result(self.folder.merge_path([save_path, "{}_不合格dialog.txt".format(name)]), data=no_dialog_lis)
            sort_res = self.sort_2(self.sort_dict(map), name)
            self.save_result(self.folder.merge_path([save_path, "{}_result.json".format(name)]), data=self.json.dumps(sort_res))


if __name__ == '__main__':
    in_path = R"D:\Desktop\1"
    save_path = R"D:\Desktop\2"
    e = Solution()
    e.process(in_path=in_path, save_path=save_path)
