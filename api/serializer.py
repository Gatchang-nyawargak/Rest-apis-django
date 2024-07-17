from rest_framework import serializers
from student.models import Student
from course.models  import Course
from teacher.models import Teacher
from classPeriod.models import ClassPeriod
from ClassProject.models import Class_Project


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = '__all__'
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
class ClassProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Project
        fields = "__all__"







