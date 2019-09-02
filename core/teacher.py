from interface import teacher_interface
from lib import common

teacher_auth={'username':None}
def login():
    while True:
        username = input('请输入登陆用户名：').strip()
        pwd = input('请输入登陆密码：').strip()
        flag,msg=teacher_interface.login_interface(username,pwd)
        if flag:
            print(msg)
            teacher_auth['username'] = username
            break
        print(msg)
        choice=input('按q退出，或者任意键继续：')
        if choice=='q':
            break

@common.login_auth('teacher')
def check_course():
    course_list=teacher_interface.check_course_interface(teacher_auth.get('username'))
    print(course_list)

@common.login_auth('teacher')
def choose_course():
    while True:
        schoolname=teacher_interface.check_school_interface(teacher_auth.get('username'))

        course_list = teacher_interface.check_course_interface(schoolname)
        if not course_list:
            print('没有课程可供选择')
            break
        for k, v in enumerate(course_list):
            print(k, v)
        choice1 = input('请输入课程编号：')
        if not choice1.isdigit():
            print('请输入数字')
            continue
        choice1 = int(choice1)
        if choice1 not in range(len(course_list)):
            continue
        msg=teacher_interface.choose_course_interface(course_list[choice1],teacher_auth.get('username'))
        print(msg)
        choice2 = input('按q退出，或者任意键继续：')
        if choice2 == 'q':
            break

@common.login_auth('teacher')
def check_student():
    while True:
        course_list = teacher_interface.check_course_interface(teacher_auth.get('username'))
        if not course_list:
            print('没有课程可供选择')
            break
        for k, v in enumerate(course_list):
            print(k, v)
        choice1 = input('请输入课程编号：')
        if not choice1.isdigit():
            print('请输入数字')
            continue
        choice1 = int(choice1)
        if choice1 not in range(len(course_list)):
            continue

        student_list = teacher_interface.check_student_interface(course_list[choice1])
        if not student_list:
            print('没有学生')
            break
        print(student_list)
        choice2 = input('按q退出，或者任意键继续：')
        if choice2 == 'q':
            break

@common.login_auth('teacher')
def chang_score():
    while True:
        course_list = teacher_interface.check_course_interface(teacher_auth.get('username'))
        if not course_list:
            print('没有课程可供选择')
            break
        for k, v in enumerate(course_list):
            print(k, v)
        choice1 = input('请输入课程编号：')
        if not choice1.isdigit():
            print('请输入数字')
            continue
        choice1 = int(choice1)
        if choice1 not in range(len(course_list)):
            continue

        student_list=teacher_interface.check_student_interface(course_list[choice1])
        if not student_list:
            print('没有学生')
            break
        for k, v in enumerate(student_list):
            print(k, v)
        choice2 = input('请输入学生编号：')
        if not choice2.isdigit():
            print('请输入数字')
            continue
        choice2 = int(choice2)
        if choice2 not in range(len(course_list)):
            continue

        score=input('请输入分数：')
        msg=teacher_interface.change_score_interface(course_list[choice1],student_list[choice2],score)
        print(msg)
        choice3 = input('按q退出，或者任意键继续：')
        if choice3== 'q':
            break


def teacher_view():
    while True:
        print('''
        0.登陆
        1.查看课程
        2.选择课程
        3.查看学生
        4.修改成绩
        q.退出
        ''')
        teacher_dic={
            '0':login,
            '1':check_course,
            '2':choose_course,
            '3':check_student,
            '4':chang_score,
        }
        choice = input('请输入功能编号：')
        if choice == 'q':
            break
        if choice in ['0', '1', '2', '3', '4']:
            teacher_dic[choice]()


