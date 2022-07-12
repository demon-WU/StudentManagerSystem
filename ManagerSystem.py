from NumException import NumException
from Menu_Student import menu_student
from Student import Student


class ManagerSystem(object):
    def __init__(self):
        # 存储数据所用的列表
        self.stuList = []
        pass
    # 主函数流程
    # 1.加载文件里面的学员数据
    # 2.显示功能菜单
    # 3.用户输入目标功能序号
    # 4.根据用户输入的序号执行不同的功能
    def run(self):
        # 加载学员信息
        self.load_student()
        while True:
            menu_student()
            try:
                menu_num = int(input('请输入相应序号执行程序:'))
                if menu_num not in [0,1,2,3,4,5,6]:
                    raise NumException(menu_num)
                pass
            except NumException as msg:
                print(msg)
                pass
            if menu_num == 1:
                # 输入1时添加一位学员信息
                self.add_student()
                pass
            elif menu_num == 2:
                # 输入2时删除一位学员信息
                self.del_student()
                pass
            elif menu_num == 3:
                # 输入3时修改学员信息
                self.update_student()
                pass
            elif menu_num == 4:
                # 输入4时查询某位学员信息
                self.select_student()
                pass
            elif menu_num == 5:
                # 输入5时显示所有学员信息
                self.sel_all_student()
                pass
            elif menu_num == 6:
                # 输入6时保存学员信息
                self.save_student()
                pass
            elif menu_num == 0:
                # 输入0时退出程序
                break
                pass
            pass
        pass
    # 输入姓名、性别、电话号码
    def add_student(self):
        '''
        添加学员信息
        :return:
        '''
        # 用户输入姓名、性别、手机号
        name = input('请输入您的姓名:')
        sex = input('请输入您的性别')
        number = input('请输入您的手机号:')
        # 创建学生对象传数据进去
        student = Student(name,sex,number)
        # 列表添加一条学员对象
        self.stuList.append(student)
        pass
    def del_student(self):
        '''
        删除学员信息
        :return:
        '''
        # 输入一个name来删除一条学员对象信息
        name = input('请输入该学员信息用于删除:')
        # 循环遍历出列表已存在的学员信息
        for i in self.stuList:
            # 校验符合条件的数据进行删除操作
            if i.name == name:
                self.stuList.remove(i)
                pass
            # 未找到学员时返回错误信息
            else:
                print('未找到该学院,请检查是否输入有误')
                pass
        pass
    def update_student(self):
        '''
        修改学员信息
        :return:
        '''
        # 根据姓名找到学员
        name = input('请输入需要修改信息的学员姓名')
        # 遍历寻找学员
        for i in self.stuList:
            if i.name == name:
                print(i.__str__)
                sex = input('修改性别为:')
                number = input('修改电话号码为:')
                i.sex = sex
                i.number = number
                pass
            else:
                print('未找到对应的学员信息,请检查')
        pass
    def select_student(self):
        '''
        查询学员信息
        :return:
        '''
        # 通过name查询员工
        name = input('请输入需要查找的学员姓名:')
        for i in self.stuList:
            if i.name == name:
                print(i.__str__)
                pass
            else:
                print('未查询到该学员信息')
                pass
        pass
    def sel_all_student(self):
        '''
        删除学员信息
        :return:
        '''
        for i in self.stuList:
            print(i.__str__)
        pass
    def save_student(self):
        '''

        :return:
        '''
        for i in self.stuList:

        pass
    def load_student(self):
        '''

        :return:
        '''
        pass