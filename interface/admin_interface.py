from db import models
import os
from conf import settings

def register_interface(username,pwd):
    class_path=os.path.join(settings.DB_PATH,'admin')
    if os.path.isdir(class_path):
        if username in os.listdir(class_path):
            return False,'用户名已存在'
    models.Admin(username,pwd)
    return True,'注册成功'


def login_interface(username,pwd):
    class_path = os.path.join(settings.DB_PATH, 'admin')
    if not os.path.isdir(class_path):
        return False,'用户不存在'
    if not username in os.listdir(class_path):
        return False,'用户不存在'
    obj=models.Admin.read(username)
    if obj.pwd!=pwd:
        return False,'密码错误'
    return True,'登陆成功'


def create_school_interface(schoolname,address):
    class_path = os.path.join(settings.DB_PATH, 'school')
    if os.path.isdir(class_path):
        if schoolname in  os.listdir(class_path):
            return '学校已存在'
    models.School(schoolname,address)
    return '创建成功'

def create_course_interface(schoolname,coursename):
    class_path = os.path.join(settings.DB_PATH, 'course')
    if os.path.isdir(class_path):
        if coursename in  os.listdir(class_path):
            return '课程已存在'
    models.Course(schoolname,coursename)
    obj=models.School.read(schoolname)
    obj.add_course(coursename)
    return '课程创建成功'



def create_teacher_interface(schoolname,teachername):
    class_path = os.path.join(settings.DB_PATH, 'teacher')
    if os.path.isdir(class_path):
        if teachername in os.listdir(class_path):
            return '用户名已存在'
    models.Teacher(schoolname, teachername)
    return '创建成功'
