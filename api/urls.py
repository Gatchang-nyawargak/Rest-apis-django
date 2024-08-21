from django.urls import path
from .views import (
    StudentListView, TeacherListView, CourseListView, 
    Class_PeriodListView, Class_ProjectListView, 
    StudentDetailView, TeacherDetailView, CourseDetailView, 
    Class_PeriodDetailView, Class_ProjectDetailView, 
    WeeklyTimetable
)





urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path('api/students/<int:pk>/', StudentDetailView.as_view(), name='student_detail_view'),
    path("teachers/", TeacherListView.as_view(), name="teacher_list_view"),
    path('api/teachers/<int:id>/', TeacherDetailView.as_view(), name='teacher_detail_view'),
    
    path("courses/", CourseListView.as_view(), name="course_list_view"),
    path('api/courses/<int:id>/', CourseDetailView.as_view(), name='course_detail_view'),
    
    path("class_periods/", Class_PeriodListView.as_view(), name="class_period_list_view"),
    path('api/class_periods/<int:id>/', Class_PeriodDetailView.as_view(), name='class_period_detail_view'),
    
    path("class_projects/", Class_ProjectListView.as_view(), name="class_project_list_view"),
    path('api/class_projects/<int:id>/', Class_ProjectDetailView.as_view(), name='class_project_detail_view'),
    
    path('weekly-timetable/', WeeklyTimetable.as_view(), name='weekly_timetable'),
]
