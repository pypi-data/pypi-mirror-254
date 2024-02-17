# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: get_img.py
@time: 2023/10/30 16:33
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
        for file, name in self.get_file(in_path, status=True):
            if ".png" in name:
                self.file.move_file(file, self.folder.merge_path([self.make_out_path(save_path, ["png"]), name]))
            if ".jpg" in name:
                self.file.move_file(file, self.folder.merge_path([self.make_out_path(save_path, ["jpg"]), name]))
            if ".json" in name:
                self.file.move_file(file, self.folder.merge_path([self.make_out_path(save_path, ["json"]), name]))


if __name__ == '__main__':
    in_path = R"D:\Desktop\4\第五批集装箱700张"
    save_path = R"E:\第五批集装箱700张_3"
    e = Solution()
    e.process(in_path=in_path, save_path=save_path)
