import os
from conf import settings
from db import models
def login_interface(username,pwd):
    class_path = os.path.join(settings.DB_PATH, 'teacher')
    if not os.path.isdir(class_path):
        return False,'用户不存在'
    if not username in os.listdir(class_path):
        return False,'用户不存在'
    obj=models.Teacher.read(username)
    if obj.pwd!=pwd:
        return False,'密码错误'
    return True,'登陆成功'

def check_course_interface(teachername):
    obj=models.Teacher.read(teachername)
    if not obj.course_list:
        return '没有选择课程'
    return obj.course_list


def choose_course_interface(coursename,teachername):
    obj=models.Teacher.read(teachername)
    if coursename in obj.course_list:
        return '课程已经存在'
    obj.choose_course(coursename)
    return '选择成功'


def check_school_interface(teachername):
    obj=models.Teacher.read(teachername)
    return obj.schoolname

def check_course_interface(teachername):
    obj=models.Teacher.read(teachername)
    if not obj.course_list:
        return None
    return obj.course_list

def check_student_interface(coursename):
    obj=models.Course.read(coursename)
    if not obj.student_list:
        return None
    return obj.student_list

def change_score_interface(coursename,studentname,score):
    obj=models.Student.read(studentname)
    obj.change_score(coursename,score)
    return '修改成功'