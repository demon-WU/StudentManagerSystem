class Student(object):
    def __init__(self, name, sex, number):
        # 姓名
        self.name = name
        # 性别
        self.sex = sex
        # 手机号码
        self.number = number
        pass

    def __str__(self):
        return "学员姓名为{}，性别为{}，手机号码为{}".format(self.name, self.sex, self.number)
    pass
