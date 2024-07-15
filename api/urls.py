from django.urls import path
from .views import StudentListView, ClassPeriodView

urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path("class-periods/", ClassPeriodView.as_view(), name="class_period_view"),
]