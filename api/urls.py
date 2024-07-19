from django.urls import path
from .views import StudentListView, ClassPeriodView, TeacherListView,CourseListView
from .views import studentDetailView
from .views import ClassProjectView
urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path("Class-Project/", ClassProjectView.as_view(), name= "class_project_view"),
    path("class-periods/", ClassPeriodView.as_view(), name="class_period_view"),
    path("course/", CourseListView.as_view(), name="course_list_view"),
    path("teachers/", TeacherListView.as_view(), name="teacher_list_view"),
    path("students/<int:id>/",studentDetailView.as_view(), name= "student_detail_view")
]