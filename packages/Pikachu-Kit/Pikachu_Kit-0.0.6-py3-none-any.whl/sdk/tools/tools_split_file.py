# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author  : v_jiaohaicheng@baidu.com
@des     :

"""

from sdk.temp.temp_supports import IsSolution
from sdk.utils.util_encrtpt import EncryptProcess


class Solution(IsSolution):
    def __init__(self, **kwargs):
        super(Solution, self).__init__()
        self.__dict__.update({k: v for k, v in [
                             i for i in locals().values() if isinstance(i, dict)][0].items()})
        self.encrypt = EncryptProcess()

    def process(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        in_path = kwargs["in_path"]
        save_path = kwargs["save_path"]
        # save_path = self.folder.merge_path([kwargs["save_path"],self.encrypt.make_uuid(1)])

        self.folder.create_folder(save_path)
        for file in self.get_file(in_path):
            num = 0
            for args in self.file.split_file(file, spliter_nums=50):
                num += 1
                # del args["headers"]

                save_path = self.folder.merge_path([kwargs["save_path"], self.encrypt.make_uuid(1)])
                self.folder.create_folder(save_path)
                self.file.save(self.folder.merge_path(
                    [save_path, "{}_{}_input.txt".format("40434", self.encrypt.make_uuid(1))]), data=args)

                # self.file.move_file("9594.exe",self.folder.merge_path([save_path,"9594.exe"]))
                # self.file.move_file("ffmpeg.exe",self.folder.merge_path([save_path,"ffmpeg.exe"]))
                # self.file.move_file(".env", self.folder.merge_path([save_path,".env"]))

                # self.file.save(self.folder.merge_path(
                #     [save_path, "{}_result.txt".format(num)]), data=args)
                # with open(self.folder.merge_path([save_path,"{}_result.txt".format(num)]),"w",encoding="utf-8")as fp:
                #     fp.write("{}\n".format("\t".join(args["headers"])))
                #     for i in args["data"]:
                #         fp.write("{}\n".format("\t".join(i)))


if __name__ == '__main__':
    in_path = R"D:\Desktop\1"
    save_path = R"D:\Desktop\3"
    e = Solution()
    e.process(in_path=in_path, save_path=save_path)
