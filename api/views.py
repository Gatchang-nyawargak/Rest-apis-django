from django.shortcuts import render
from api.serializer import StudentSerializer, ClassPeriodSerializer, CourseSerializer, TeacherSerializer,ClassProjectSerializer
from rest_framework import status
from student.models import Student

from teacher.models import Teacher
from course.models import Course
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StudentSerializer
from .serializer import ClassPeriodSerializer
from .serializer import TeacherSerializer
from .serializer import CourseSerializer
from classPeriod.models import ClassPeriod
from ClassProject.models import Class_Project



          
          

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        country = request.query_params.get("country")  

        if first_name:
            students = students.filter(first_name=first_name)
        if country: 
            students = students.filter(country=country)
        
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
             
class studentDetailView(APIView):
    def get(self, request, id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def enroll(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.courses.add(course)

    def post(self, request, id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")
        if action == "enroll":
           course_id = request.data.get("course_id")
           self.enroll(student, course_id)
        return Response(status=status.HTTP_201_CREATED)

            
class ClassPeriodView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data)
class ClassListView(APIView):
    def get(self, request):
        classPeriod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classPeriod,many=True)
        return Response(serializer.data)
class ClassDetailView(APIView):
    def get(self, request, id):
        classPeriod = ClassPeriod.objects.get(id = id)
        serializer = ClassPeriodSerializer(classPeriod)
        return Response(serializer.data)
    def post(self,request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        classPeriod= ClassPeriod.objects.get(id=id)
        serializer =StudentSerializer (classPeriod)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,id):
        classPeriod =ClassPeriod.objects.get(id=id)
        classPeriod.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
            
            
class TeacherView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
            
    
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)


    
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        teacher= Teacher.objects.get(id=id)
        serializer =TeacherSerializer(teacher)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request,id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
    
class CourseView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)   
class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    
class CourseDetailView(APIView):
    def get(self, request, id):
        course = Course.objects.get(id = id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


    
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        course= Course.objects.get(id=id)
        serializer =CourseSerializer(course)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
    
class ClassProjectView(APIView):
    def get(self, request):
        class_Project = Class_Project.objects.all()
        serializer = ClassProjectSerializer(Class_Project, many = True)
        return Response(serializer)
class ClassProjectListView(APIView):
    def get(self, request):
        classProject = Class_Project.objects.all()
        serializer = ClassProjectSerializer(classProject, many=True)
        return Response(serializer.data)
    
class ClassProjectDetailView(APIView):
    def get(self, request, id):
        classProject = Class_Project.objects.get(id = id)
        serializer = ClassProjectSerializer(classProject)
        return Response(serializer.data)


    
    def post(self,request):
        serializer = ClassProjectSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,id):
        classProject= Class_Project.objects.get(id=id)
        serializer =ClassProjectSerializer(classProject)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,id):
        classProject = Class_Project.objects.get(id=id)
        classProject.delete()
        return Response (status=status.HTTP_202_ACCEPTED)


class WeeklyTimetableView(APIView):
    def get(self, request):
        timetable = {}
        class_periods = ClassPeriod.objects.all()

        for class_period in class_periods:
            day = class_period.day_of_week
            if day not in timetable:
                timetable[day] = []
            
            timetable[day].append({
                "teacher": class_period.teacher.name,
                "course": class_period.course.name,
                "start_time": class_period.start_time,
                "end_time": class_period.end_time,
            })
        
        return Response(timetable, status=status.HTTP_200_OK)
