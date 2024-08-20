from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import StudentSerializer, ClassPeriodSerializer, CourseSerializer, TeacherSerializer, ClassProjectSerializer,  MinimalStudentSerializer, MinimalTeacherSerializer,MinimalCourseSerializer, MinimalClassPeriodSerializer, MinimalClassProjectSerializer
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from classPeriod.models import ClassPeriod
from ClassProject.models import Class_Project

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            students = students.filter(first_name=first_name)
        country = request.query_params.get("country")
        if country:
            students = students.filter(country=country)
        serializer = MinimalStudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")
        if action == "enroll":
            course_id = request.data.get("course_id")
            self.enroll(student, course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "unenroll":
            course_id = request.data.get("course_id")
            self.unenroll(student, course_id)
            return Response(status=status.HTTP_200_OK)
        elif action == "add_to_class":
            class_id = request.data.get("class_id")
            self.add_to_class(student, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def enroll(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.courses.add(course)

    def unenroll(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.courses.remove(course)

    def add_to_class(self, student, class_id):
        student_class = Class_Project.objects.get(id=class_id)
        student_class.students.add(student)

class Class_ProjectListView(APIView):
    def get(self, request):
        student_classes = Class_Project.objects.all()
        serializer = MinimalClassProjectSerializer(student_classes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Class_ProjectDetailView(APIView):
    def get(self, request, id):
        student_class = Class_Project.objects.get(id=id)
        serializer = ClassProjectSerializer(student_class)
        return Response(serializer.data)

    def put(self, request, id):
        student_class = Class_Project.objects.get(id=id)
        serializer = ClassProjectSerializer(student_class, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student_class = Class_Project.objects.get(id=id)
        student_class.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = MinimalTeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id):
        teacher = Teacher.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_course":
            course_id = request.data.get("course_id")
            self.assign_course(teacher, course_id)
            return Response(status=status.HTTP_201_CREATED)
        elif action == "assign_class":
            class_id = request.data.get("class_id")
            self.assign_class(teacher, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def assign_course(self, teacher, course_id):
        course = Course.objects.get(id=course_id)
        teacher.courses.add(course)

    def assign_class(self, teacher, class_id):
        student_class = Class_Project.objects.get(id=class_id)
        student_class.teacher = teacher
        student_class.save()

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = MinimalCourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Class_PeriodListView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = MinimalClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Class_PeriodDetailView(APIView):
    def get(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(class_period)
        return Response(serializer.data)

    def put(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(class_period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        class_period.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id):
        action = request.data.get("action")
        if action == "create_class_period":
            teacher_id = request.data.get("teacher_id")
            course_id = request.data.get("course_id")
            self.create_class_period(teacher_id, course_id)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def create_class_period(self, teacher_id, course_id):
        teacher = Teacher.objects.get(id=teacher_id)
        course = Course.objects.get(id=course_id)
        class_period = ClassPeriod(teacher=teacher, course=course)
        class_period.save()
class WeeklyTimetable(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
