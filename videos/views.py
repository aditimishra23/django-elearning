from django.shortcuts import render
from django.views.generic import *
from .models import *

class CourseListView(ListView):
	model = Course
	context_object_name = 'courses'
	template_name = 'videos/list_course.html'

class VideoListView(ListView):
	model = Video
	context_object_name = 'videos'
	template_name = 'videos/list_video.html'

class CourseDetailView(DetailView):
	model = Course
	context_object_name = 'course'
	template_name = 'videos/course_detail.html'

	def get_context_data(self, **kwargs):			
		context = super(CourseDetailView, self).get_context_data(**kwargs)
		context['teacher'] = Teacher.objects.get(pk=self.kwargs['pk'])
		return context
