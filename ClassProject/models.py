from django.db import models
from student.models import Student
from django.db.models.manager import BaseManager


from django.db import models

class Class_Project(models.Model):
    no_of_students = models.IntegerField(default=0) 
    class_name = models.CharField(max_length=100)
    class_code = models.AutoField(primary_key=True)
    room_allocation = models.CharField(max_length=100)
    no_of_tables = models.PositiveSmallIntegerField(default=0)
    class_representative = models.CharField(max_length=255, default='N/A')
    class_goals = models.TextField()
    class_meeting = models.CharField(max_length=100, default='Monday')
    period_entity = models.CharField(max_length=100)
    
    
    objects: BaseManager["Class_Project"]


    # course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.class_name}"
    


