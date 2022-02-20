class Teacher:
    def teacher_task(self):
        print("I teach")

class Student:
    def student_task(self):
        print('I study')

class youtuber:
    def youtuber_task(self):
        print("I make videos")

class person(Teacher,Student,youtuber):
    def person_task(self):
        print("I can be a teacher, student or/and youtuber")

p = person()
p.student_task()
p.youtuber_task()
p.teacher_task()
p.person_task()