from interface import student_interface
from lib import common

student_auth={'username':None}
def register():
    while True:
        username=input('请输入注册用户名：').strip()
        pwd=input('请输入注册密码：').strip()
        re_pwd=input('请再次输入密码：').strip()
        if pwd!=re_pwd:
            print('密码不止一次')
            continue
        flag,msg=student_interface.register_interface(username,pwd)
        if flag:
            print(msg)
            break
        print(msg)
        break


def login():
    while True:
        username = input('请输入登陆用户名：').strip()
        pwd = input('请输入登陆密码：').strip()
        flag,msg=student_interface.login_interface(username,pwd)
        if flag:
            print(msg)
            student_auth['username']=username
            break
        print(msg)
        choice=input('按q退出，或者任意键继续：')
        if choice=='q':
            break



@common.login_auth('student')
def choose_school():
    while True:
        school_list=common.list_school()
        if not school_list:
            print('没有学校可供选择')
            break
        for k,v in enumerate(school_list):
            print(k,v)
        choice = input('请输入学校编号：')
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)
        if choice not in range(len(school_list)):
            continue
        msg=student_interface.choose_school_interface(school_list[choice],student_auth.get('username'))
        print(msg)
        choice1 = input('按q退出，或者任意键继续：')
        if choice1 == 'q':
            break



@common.login_auth('student')
def choose_course():
    while True:
        schoolname=student_interface.check_school(student_auth.get('username'))
        if not schoolname:
            print('请先选择学校')
            break
        course_list=student_interface.check_course(schoolname)
        if not course_list:
            print('没有课程可供选择')
            break
        for k,v in enumerate(course_list):
            print(k,v)
        choice1 = input('请输入课程编号：')
        if not choice1.isdigit():
            print('请输入数字')
            continue
        choice1 = int(choice1)
        if choice1 not in range(len(course_list)):
            continue
        msg=student_interface.choose_course_interface(course_list[choice1],student_auth.get('username'))
        print(msg)
        choice2 = input('按q退出，或者任意键继续：')
        if choice2 == 'q':
            break

@common.login_auth('student')
def check_score():
    course_dic=student_interface.check_score_interface(student_auth.get('username'))
    print(course_dic)



def student_view():
    while True:
        print('''
        0.注册
        1.登陆
        2.选择学校
        3.选择课程
        4.查看成绩
        q.退出
        ''')
        student_dic={
            '0':register,
            '1':login,
            '2':choose_school,
            '3':choose_course,
            '4':check_score,
        }
        choice = input('请输入功能编号：')
        if choice == 'q':
            break
        if choice in ['0', '1', '2', '3', '4']:
            student_dic[choice]()



