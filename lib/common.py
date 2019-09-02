import os
from conf import settings
def list_school():
    class_path=os.path.join(settings.DB_PATH,'school')
    if not os.path.isdir(class_path):
        return None
    return os.listdir(class_path)

def list_course():
    class_path = os.path.join(settings.DB_PATH, 'course')
    if not os.path.isdir(class_path):
        return None
    return os.listdir(class_path)

def login_auth(type):
    def outer(func):
        from core import admin,student,teacher
        def inner(*args,**kwargs):
            if type=='admin':
                if not admin.admin_auth.get('username'):
                    admin.login()
                    res = func(*args, **kwargs)
                    return res
                res=func(*args,**kwargs)
                return res
            elif type == 'student':
                if not student.student_auth.get('username'):
                    student.login()
                    res = func(*args, **kwargs)
                    return res
                res = func(*args, **kwargs)
                return res

            elif type == 'teacher':
                if not teacher.teacher_auth.get('username'):
                    teacher.login()
                    res = func(*args, **kwargs)
                    return res
                res = func(*args, **kwargs)
                return res

        return inner
    return outer