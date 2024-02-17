# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: merge_sort.py
@time: 2023/11/1 17:25
@desc:

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
        repeat_lis = []
        map = {}
        _name = "合并"
        for file, name in self.get_file(in_path, status=True):
            print(file, name)
            for args in self.file.read_json_file(file):
                # print(args)
                image = args["image"]
                kind, key1, key2 = image.split(".")[0].split("/")[-1].split("-")

                if map.get(key1) is None:
                    map[key1] = {
                        key2: self.json.dumps(args)
                    }
                else:
                    if map[key1].get(key2) is None:
                        map[key1][key2] = self.json.dumps(args)
                    else:
                        # print("重复：{}".format(image))
                        repeat_lis.append([name, image])

        result = self.sort_2(self.sort_dict(map), _name)
        if repeat_lis:
            self.save_result(self.folder.merge_path([save_path, "{}_重复.txt".format(_name)]), data=repeat_lis)

        self.save_result(self.folder.merge_path([save_path, "{}_result.json".format(_name)]), data=self.json.dumps(result))


if __name__ == '__main__':
    in_path = R"D:\Desktop\1"
    save_path = R"D:\Desktop\2"
    e = Solution()
    e.process(in_path=in_path, save_path=save_path)
