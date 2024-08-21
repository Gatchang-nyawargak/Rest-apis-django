from datetime import date
import datetime
from rest_framework import serializers
from student.models import Student
from course.models  import Course
from teacher.models import Teacher
from classPeriod.models import ClassPeriod
from ClassProject.models import Class_Project
from rest_framework import serializers
from datetime import datetime, date



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
class MinimalTeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self, object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model = Teacher
        fields = ['id', 'full_name','email']
class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_description', 'course_teacher']
class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
       model = Course
       fields = ['id', 'name','teacher']
class ClassProjectSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    class Meta:
        model =Class_Project
        fields = "__all__"
class MinimalClassProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Project
        fields = ['id', 'name','capacity']
class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many = True)
    class_enrolled = ClassProjectSerializer()
    courses = CourseSerializer(many=True, read_only=True) 

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'courses']
    
class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def get_age(self, obj):
        if obj.date_of_birth:
            today = datetime.now()
            
            if isinstance(obj.date_of_birth, date) and not isinstance(obj.date_of_birth, datetime):
                date_of_birth = datetime.combine(obj.date_of_birth, datetime.min.time())
            else:
                date_of_birth = obj.date_of_birth
            
       
            age = today - date_of_birth
            return age.days // 365
        return None 

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email', 'age']
class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = '__all__'

class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = ['id', 'name', 'start_time', 'end_time']
