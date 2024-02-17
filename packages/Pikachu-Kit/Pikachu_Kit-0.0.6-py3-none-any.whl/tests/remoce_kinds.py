# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: remoce_kinds.py
@time: 2023/10/31 13:53
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
            # print(file, name)
            lis = []
            for args in self.file.read_json_file(file):
                # print(args)
                image = args["image"]
                if "B/" not in image:
                    lis.append(args)

                # break

            self.save_result(self.folder.merge_path([save_path, "{}_result.json".format(name)]), data=self.json.dumps(lis))


if __name__ == '__main__':
    in_path = R"D:\Desktop\1"
    save_path = R"D:\Desktop\2"
    e = Solution()
    e.process(in_path=in_path, save_path=save_path)
