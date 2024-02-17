# -- coding: utf-8 --
# @Time    : 2024/1/31 10:26
# @Author  : TangKai
# @Team    : ZheChengData

class SubwaySim(object):
    def __init__(self, name: str = 'tk'):
        self.name = name

    def get_info(self):
        print(rf'{self.name}Ready to go!')
