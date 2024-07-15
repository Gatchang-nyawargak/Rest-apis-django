from django.db import models
from course.models import Course
from django.db.models.manager import BaseManager
from django.db import models
from datetime import time


# Create your models here.

class ClassPeriod(models.Model):
    ## Class Period Details
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=20)
    
    objects: BaseManager["ClassPeriod"]

    ## Relationship to Course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='class_periods')
    classroom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.day_of_week} ({self.start_time} - {self.end_time})"
