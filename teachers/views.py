from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin

class TeacherRegisterView(SuccessMessageMixin,CreateView):
	template_name = 'teachers/register.html'
	form_class = TeacherRegisterForm
	success_url = '/'
	success_message = 'Your account has successfully been registered!'

	def form_valid(self, form):
		user = form.save(commit=False)		
		user.save()
		return redirect(self.success_url)

class HomeView(TemplateView):
	context_object_name = 'teachers'
	template_name = 'teachers/index.html'

class TeacherListView(ListView):
	model = Teacher
	context_object_name = 'teachers'
	template_name = 'teachers/list.html'

class TeacherDetailView(DetailView):
	model = Teacher
	context_object_name = 'teacher'
	template_name = 'teachers/detail.html'
