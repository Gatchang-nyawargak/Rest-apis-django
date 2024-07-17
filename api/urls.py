from django.urls import path
from .views import StudentListView, ClassPeriodView, TeacherListView,CourseListView
urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path("class-periods/", ClassPeriodView.as_view(), name="class_period_view"),
    path("course/", CourseListView.as_view(), name="course_list_view"),
    path("teachers/", TeacherListView.as_view(), name="teacher_list_view"),
]