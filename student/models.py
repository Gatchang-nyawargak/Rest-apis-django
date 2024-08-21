from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    code = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    bio = models.TextField()
    parent_name = models.CharField(max_length=50)
    parent_contact = models.CharField(max_length=20) 
    enrolled_courses = models.ManyToManyField('course.Course')

    objects = models.Manager()  
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
