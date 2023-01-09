from django.db import models

# Create your models here.

# Vamos a crear 4 modelos:
# 1 -> Person
# 2 -> Student
# 3 -> Teacher
# 4 -> Classroom

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    born_date = models.DateField()

    class Meta:
        abstract = True


class Classroom(models.Model):
    name = models.CharField(max_length=2)
    start_time = models.TimeField()

    def __str__(self): # cuando uso el Classroom.object.all() me devuelve el nombre y la hora de inicio
        return self.name + " " + str(self.start_time)

    class Meta:
        db_table = 'classrooms'

class ClassroomProxy(Classroom):
    class Meta:
        proxy = True 
        ordering = ['name']


class Student(Person):
    classroomId = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    lab_grade = models.FloatField(default=0.0)
    exam_grade = models.FloatField(default=0.0)
    final_grade = models.FloatField(default=0.0)

    class Meta:
        db_table = 'students'


class StudentProxy(Student): 
    class Meta:
        ordering = ["id"]   
        proxy = True 

    def average_grades(self):
        return (self.lab_grade + self.exam_grade + self.final_grade) / 3


class Teacher(Person):
    salary = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)

    class Meta:
        db_table = 'teachers'


class TeacherProxy(Teacher):
    class Meta:
        proxy = True 

    def get_bonus(self):
        return self.salary + (100 * self.rating)
    
