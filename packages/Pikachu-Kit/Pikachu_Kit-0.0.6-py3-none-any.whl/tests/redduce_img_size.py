# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: redduce_img_size.py
@time: 2023/10/24 15:35
@desc:

"""
import os
import traceback

from PIL import Image
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

        self.error_list = []

        for file in self.get_file(in_path):

            # for args in self.read_line(file):
            #     print(args)
            self.process_img(file, save_path)

        if self.error_list:
            self.save_result("错误图片.txt", data=self.error_list, headers=["图片路径", "异常原因"])

    def process_img(self, file, save_path):
        file_split = self.folder.split_path(file)

        save_folder = file_split[-3:-1]
        name = file_split[-1]
        # print(save_folder,name)
        # # 打开图像
        # input_image = Image.open(file)
        #
        # # 降低图像的压缩质量（0-100之间，100为最高质量）
        # compression_quality = 80  # 你可以根据需要调整这个值
        # # 保存图像时指定压缩质量
        # input_image.save(self.folder.merge_path([save_path,name]), quality=compression_quality)
        #
        # # 关闭图像文件
        # input_image.close()

        save_path = self.make_out_path(save_path, save_folder)
        print("save_path", save_path)

        try:
            image = Image.open(file)
            if not os.path.exists(self.folder.merge_path([save_path, name]) + ".webp"):
                try:
                    image.save(self.folder.merge_path([save_path, name]) + ".webp", optimize=True)
                    os.rename(self.folder.merge_path([save_path, name]) + ".webp",
                              self.folder.merge_path([save_path, name]))
                except BaseException:
                    msg = "异常图片:{},异常原因:{}".format(file, traceback.print_exc())
                    print(msg)
                    self.error_list.append([file, "未知"])
            else:
                msg = "异常图片:{},异常原因:{}".format(file, "重复")
                print(msg)
                self.error_list.append([file, "重复"])
        except BaseException:
            msg = "异常图片:{},异常原因:{}".format(file, "损坏")
            print(msg)
            self.error_list.append([file, "损坏"])


if __name__ == '__main__':
    in_path = R"D:\Desktop\6"
    save_path = R"D:\Desktop\7"
    e = Solution()
    e.process(in_path=in_path, save_path=save_path)
