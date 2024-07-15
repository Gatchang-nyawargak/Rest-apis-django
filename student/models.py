from django.db import models
from django.db.models.manager import BaseManager


# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name =models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    email =models.EmailField()
    code =models.PositiveSmallIntegerField()
    date_of_birth =models.DateField()
    country = models.CharField(max_length=20)
    bio =models.TextField()
    parentName = models.CharField(max_length=50)
    parentContact = models.CharField(max_length=20)
    
    
    objects: BaseManager["Student"]
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
    
