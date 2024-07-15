from django.db import models
from student.models import Student


# Create your models here.
class Class_project(models.Model):
    class_students = models.ManyToManyField(Student, related_name='class_projects')
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=50)
    class_description = models.TextField()
    class_start_date = models.DateField()
    class_end_date = models.DateField()
    class_capacity = models.IntegerField()
    class_status = models.CharField(max_length=20)
    class_location = models.CharField(max_length=50)
    class_time = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.class_name}"
    