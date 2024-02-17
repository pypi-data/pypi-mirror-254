# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: __init__.py.py
@time: 2023/11/25 10:35
@desc:

"""

from sdk.temp.temp_supports import IsSolution


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
        for file in self.get_file(in_path):
            for args in self.read_line(file):
                data = self.get_column(args, [*, *])


if __name__ == '__main__':
    in_path = R"E:\Desktop\1"
    save_path = R"E:\Desktop\2"
    e = Solution()
    e.process(in_path=in_path, save_path=save_path)
