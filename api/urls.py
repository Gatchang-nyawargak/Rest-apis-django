from django.urls import path
from .views import StudentListView, ClassPeriodListView, TeacherListView, CourseListView
from .views import WeeklyTimetable

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
    path('class-periods/', ClassPeriodListView.as_view(), name='class-period-list'),
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('views/timetable/', WeeklyTimetable.as_view(), name='weekly-timetable'),
    
    
]
