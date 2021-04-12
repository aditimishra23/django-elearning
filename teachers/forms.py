from django import forms
from django.contrib.auth.forms import *
from .models import *

class TeacherRegisterForm(forms.ModelForm):
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=50)
	password1 = forms.CharField()
	password2 = forms.CharField()

	class Meta(UserCreationForm):
		model = Teacher
		fields = ('first_name','last_name','email','password1','password2')

