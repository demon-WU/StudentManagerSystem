# 导入管理系统模块
from ManagerSystem import *

# 保证是当前文件运行才启动管理系统
if __name__ == '__main__':
    student_managerSystem = ManagerSystem()
    student_managerSystem.run()