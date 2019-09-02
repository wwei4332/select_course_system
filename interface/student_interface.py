from db import models
import os
from conf import settings

def register_interface(username,pwd):
    class_path=os.path.join(settings.DB_PATH,'student')
    if os.path.isdir(class_path):
        if username in os.listdir(class_path):
            return False,'用户名已存在'
    models.Student(username,pwd)
    return True,'注册成功'




def login_interface(username,pwd):
    class_path = os.path.join(settings.DB_PATH, 'student')
    if not os.path.isdir(class_path):
        return False,'用户不存在'
    if not username in os.listdir(class_path):
        return False,'用户不存在'
    obj=models.Admin.read(username)
    if obj.pwd!=pwd:
        return False,'密码错误'
    return True,'登陆成功'


def choose_school_interface(schoolname,studentname):
    obj=models.Student.read(studentname)
    if  obj.schoolname:
        return '已经选择了学校'
    obj.choose_school(schoolname)
    return '选择成功'

def choose_course_interface(coursename,studentname):
    obj=models.Student.read(studentname)
    if obj.course_dic.get(coursename):
        return '课程已经选择过了'
    obj.choose_course(coursename)
    obj_course=models.Course.read(coursename)
    obj_course.add_student(studentname)
    return '选择成功'

def check_score_interface(studentname):
    obj=models.Student.read(studentname)
    if not obj.course_dic:
        return '没有选择课程'
    return obj.course_dic


def check_school(studentname):
    obj=models.Student.read(studentname)
    if not obj.schoolname:
        return None
    return obj.schoolname

def check_course(schoolname):
    obj=models.School.read(schoolname)
    if not obj.course_list:
        return None
    return obj.course_list
