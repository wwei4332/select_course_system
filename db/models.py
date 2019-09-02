import os
from conf import  settings
from db import  db_handler
class Base:
    def save(self):
        db_handler.save(self)
    @classmethod
    def read(cls,name):
        return db_handler.read(cls,name)


class Admin(Base):
    def __init__(self,name,pwd):
        self.name=name
        self.pwd=pwd
        self.save()

class School(Base):
    def __init__(self,schoolname,address):
        self.name=schoolname
        self.address=address
        self.course_list=[]
        self.teacher_list=[]
        self.save()
    def add_course(self,coursename):
        self.course_list.append(coursename)
        self.save()



class Course(Base):
    def __init__(self,schoolname,coursename):
        self.schoolname=schoolname
        self.name=coursename
        self.student_list=[]
        self.save()
    def add_student(self,studentname):
        self.student_list.append(studentname)
        self.save()

class Teacher(Base):
    def __init__(self,schoolname,teachername):
        self.schoolname=schoolname
        self.pwd='123'
        self.name=teachername
        self.course_list=[]
        self.save()
    def choose_course(self,coursename):
        self.course_list.append(coursename)
        self.save()


class Student(Base):
    def __init__(self,studentname,pwd):
        self.schoolname=None
        self.name=studentname
        self.pwd=pwd
        self.course_dic={}
        self.save()
    def choose_school(self,schoolname):
        self.schoolname=schoolname
        self.save()
    def choose_course(self,coursename):
        self.course_dic[coursename]=0
        self.save()
    def change_score(self,coursename,score):
        self.course_dic[coursename]=score
        self.save()