from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

class Teacher(models.Model):
	email = models.EmailField(_('email address'), unique=True)
	image = models.ImageField(upload_to='media/teachers',default='media/teachers/default.png')
	first_name = models.CharField(_('first name'),max_length=50, blank=False)
	last_name = models.CharField(_('last name'),max_length=50, blank=False)
	subject = models.CharField(_('subject'),max_length=20,blank=False,default=None)	
	description = RichTextField(blank=True)
	is_active = models.BooleanField(_('active'),default=True)

	def __str__(self):
		return self.email
