from django.db import models
from student.models import Student
from teacher.models import Teacher
from django.db.models.manager import BaseManager



# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    course_description = models.TextField()
    course_credits = models.IntegerField()
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    course_status = models.CharField(max_length=20)
    course_location = models.CharField(max_length=50)
    course_time = models.CharField(max_length=20)
    course_students = models.ManyToManyField(Student, related_name='courses')
    course_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    
    objects: BaseManager["Course"]

    def __str__(self):
        return f"{self.course_name}"


