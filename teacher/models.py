from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    qualifications = models.TextField()
    teacher_status = models.CharField(max_length=20)
    enrollment_date = models.DateField()
    teacher_photo = models.ImageField(upload_to='teacher_photos')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"