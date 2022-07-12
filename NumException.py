# 输入非法异常类
class NumException(Exception):
    def __init__(self,menu_num):
        self.menu_num = menu_num
        pass
    def __str__(self):
        return "输入非法{}，请重新输入".format(self.menu_num)
