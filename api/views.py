from django.shortcuts import render
from student.models import Student
from classPeriod.models import ClassPeriod
from .serializer import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StudentSerializer
from .serializer import ClassPeriodSerializer


class StudentListView(APIView):
    def get(self, request):
       students = Student.objects.all()
       serializer = StudentSerializer(students, many=True)
       return Response(serializer.data)
    


class ClassPeriodView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data)