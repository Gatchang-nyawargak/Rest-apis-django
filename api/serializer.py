# from student.models import Student
# from rest_framework import  serializers
# from classPeriod.models import ClassPeriod

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = "__all__"



# class ClassPeriodSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ClassPeriod
#         fields = ['start_time', 'end_time', 'day_of_week', 'course', 'classroom']

from rest_framework import serializers
from student.models import Student
from classPeriod.models import ClassPeriod

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = '__all__'
        