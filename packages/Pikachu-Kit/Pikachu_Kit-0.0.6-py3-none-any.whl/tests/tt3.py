# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: tt3.py
@time: 2023/10/31 15:21
@desc:

"""

from sdk.temp.temp_supports import IsSolution
from urllib.parse import unquote


class Solution(IsSolution):
    def __init__(self, **kwargs):
        super(Solution, self).__init__()
        self.__dict__.update({k: v for k, v in [
            i for i in locals().values() if isinstance(i, dict)][0].items()})

    def process(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        in_path = kwargs["in_path"]
        save_path = kwargs["save_path"]
        self.folder.create_folder(save_path)
        for file, name in self.get_file(in_path, status=True):
            print(file, name)
            lis = []
            for args in self.read_line(file):
                # print(args)
                args["line"][args["headers"].index("url")] = unquote(args["line"][args["headers"].index("url")])
                url = args["line"][args["headers"].index("url")]
                # print(url)
                lis.append(args["line"])
            self.save_result(self.folder.merge_path([save_path, "乱码处理.txt"]), data=lis, headers=['file_name', 'url', '描述一', '描述二', '描述三', '描述四', '描述五'])


if __name__ == '__main__':
    in_path = R"D:\Desktop\1"
    save_path = R"D:\Desktop\2"
    e = Solution()
    e.process(in_path=in_path, save_path=save_path)
