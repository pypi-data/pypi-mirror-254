# !/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: JHC000abc@gmail.com
@file: test.py
@time: 2023/11/29 15:25
@desc:

"""
from sdk.temp.temp_supports import IsSolution
from supports.text_process.parse_html import HtmlParser


class Solution(IsSolution):
    """
    Solution
    """

    def __init__(self, **kwargs):
        """
        初始化函数
        :param kwargs: 字典类型的参数字典，包含可选的关键字参数
        """
        super(Solution, self).__init__()
        self.__dict__.update({k: v for k, v in [
            i for i in locals().values() if isinstance(i, dict)][0].items()})

    def process(self, **kwargs):
        """
        处理文件

        :param kwargs: 关键字参数
        :return: 无返回值
        """
        in_path = kwargs["in_path"]  # 输入文件路径
        save_path = kwargs["save_path"]  # 保存文件路径
        self.folder.create_folder(save_path)  # 创建保存文件的文件夹
        for file, name in self.get_file(in_path, status=True):
            out_lis = []
            with open(file, "r", encoding="utf-8") as f:
                for i in f:
                    data = self.json.loads(i.strip())
                    print(data.keys())
                    print(data["id"])
                    print(data["url"])
                    print(data["spider_time"])
                    save_file = self.folder.merge_path([save_path, "{}_{}.html".format(data["id"], data["spider_time"].replace(":", "-"))])
                    with open(save_file, "w", encoding="utf-8") as f:
                        f.write(data["content"])

                    out_lis.append([str(data["id"]), data["url"], data["spider_time"], save_file])

            self.save_result(self.folder.merge_path([save_path, "{}_.txt".format(name)]), out_lis, headers=["id", "url", "spider_time", "save_file"])

    def process2(self, **kwargs):
        in_path = kwargs["in_path"]  # 输入文件路径
        save_path = kwargs["save_path"]  # 保存文件路径
        self.folder.create_folder(save_path)  # 创建保存文件的文件夹
        for file, name in self.get_file(in_path, status=True):
            # file = R"D:\Desktop\1\1_2023-02-10 16-30-03.html"
            with open(file, "r+", encoding="utf-8") as fp:
                content = fp.read()
            content = content.encode('utf-8', 'xmlcharrefreplace').decode('utf-8')
            res = HtmlParser.main(content)

            with open(self.folder.merge_path([save_path, "result_{}.json".format(name)]), "w", encoding="utf-8") as f:
                f.write(self.json.dumps(res))


if __name__ == '__main__':
    in_path = R"D:\Desktop\1"
    save_path = R"D:\Desktop\2"
    e = Solution()
    # e.process(in_path=in_path, save_path=save_path)
    e.process2(in_path=in_path, save_path=save_path)
