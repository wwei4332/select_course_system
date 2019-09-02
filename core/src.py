from core import admin,student,teacher
while True:
    print('''
    0.管理员视图
    1.学生视图
    2.老师视图
    q.退出
    ''')
    view_dic={
        '0':admin.admin_view,
        '1':student.student_view,
        '2':teacher.teacher_view,

    }
    choice = input('请输入功能编号：')
    if choice == 'q':
        break
    if choice in ['0', '1', '2',]:
        view_dic[choice]()