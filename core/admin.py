from interface import admin_interface
from lib import common

admin_auth={'username':None}
def register():
    while True:
        username=input('请输入注册用户名：').strip()
        pwd=input('请输入注册密码：').strip()
        re_pwd=input('请再次输入密码：').strip()
        if pwd!=re_pwd:
            print('密码不止一次')
            continue
        flag,msg=admin_interface.register_interface(username,pwd)
        if flag:
            print(msg)
            admin_auth['username']=username
            break
        print(msg)
        break


def login():
    while True:
        username = input('请输入登陆用户名：').strip()
        pwd = input('请输入登陆密码：').strip()
        flag,msg=admin_interface.login_interface(username,pwd)
        if flag:
            print(msg)
            admin_auth['username'] = username
            break
        print(msg)
        choice=input('按q退出，或者任意键继续：')
        if choice=='q':
            break

@common.login_auth('admin')
def create_school():
    while True:
        schoolname=input('请输入学校名称：').strip()
        address=input('请输入学校地址：').strip()
        msg=admin_interface.create_school_interface(schoolname,address)
        print(msg)
        choice = input('按q退出，或者任意键继续：')
        if choice == 'q':
            break

@common.login_auth('admin')
def create_course():
    while True:
        school_list=common.list_school()
        if not school_list:
            print('请先创建学校')
            break
        for k,v in enumerate(school_list):
            print(k,v)
        choice=input('请输入学校编号：')
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice=int(choice)
        if choice not in range(len(school_list)):
            continue
        coursename=input('请输入课程名称:').strip()
        msg=admin_interface.create_course_interface(school_list[choice],coursename)
        print(msg)
        choice = input('按q退出，或者任意键继续：')
        if choice == 'q':
            break

@common.login_auth('admin')
def create_teacher():
    while True:
        school_list = common.list_school()
        if not school_list:
            print('请先创建学校')
            break
        for k, v in enumerate(school_list):
            print(k, v)
        choice = input('请输入学校编号：')
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)
        if choice not in range(len(school_list)):
            continue
        teachername=input('请输入老师用户名：')
        msg=admin_interface.create_teacher_interface(school_list[choice],teachername)
        print(msg)
        choice = input('按q退出，或者任意键继续：')
        if choice == 'q':
            break



def admin_view():
    while True:
        print('''
        0.注册
        1.登陆
        2.创建学校
        3.创建课程
        4.创建老师
        q.退出
        ''')
        admin_dic={
            '0':register,
            '1':login,
            '2':create_school,
            '3':create_course,
            '4':create_teacher,
        }
        choice=input('请输入功能编号：')
        if choice=='q':
            break
        if choice in ['0','1','2','3','4']:
            admin_dic[choice]()