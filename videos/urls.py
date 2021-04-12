from django.urls import path,include
from .views import *

app_name = 'videos'

urlpatterns = [
	path('list',CourseListView.as_view(),name='list'),
	path('course-detail/<int:pk>/',CourseDetailView.as_view(),name='course_detail'),
]