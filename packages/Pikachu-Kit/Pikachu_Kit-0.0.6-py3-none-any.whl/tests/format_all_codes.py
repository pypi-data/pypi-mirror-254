# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: format_all_codes.py
@time: 2023/11/21 13:24
@desc:

"""
import os
from sdk.temp.temp_supports import IsSolution


class Solution(IsSolution):
    """
    Solution
    """

    def __init__(self, **kwargs):
        """

        """
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
            if "venv" not in file:
                if name.endswith(".py"):
                    cmd = R"D:\Project\Python\Project_Fastapi\venv\Scripts\autopep8.exe --in-place --aggressive --ignore=E123,E133,E50 {}".format(file)
                    print(cmd)
                    os.system(cmd)
                elif name.endswith(".pyc"):
                    os.remove(file)


if __name__ == '__main__':
    in_path = R"D:\Project\Python\pythondevelopmenttools"
    save_path = R"D:\Desktop\2"
    e = Solution()
    e.process(in_path=in_path, save_path=save_path)
