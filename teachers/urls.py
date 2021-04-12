from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('teacher-list/',TeacherListView.as_view(),name='teacher_list'),
    path('teacher-detail/<int:pk>/',TeacherDetailView.as_view(),name='teacher_detail'),
    path('register/',TeacherRegisterView.as_view(),name='register')
]