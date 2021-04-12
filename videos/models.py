from django.db import models
from teachers.models import Teacher
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify 
from ckeditor.fields import RichTextField

class Course(models.Model):
	title = models.CharField(_('title'),max_length=100,blank=False)
	subject = models.CharField(_('subject'),max_length=20,blank=False,default=None)
	teacher =  models.ForeignKey(Teacher,on_delete=models.CASCADE,default=None,blank=False)
	description = RichTextField(blank=False)
	slug = models.SlugField(_('slug'),unique=True,default=None, editable=False)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Course, self).save(*args, **kwargs)

class Test(models.Model):
	title = models.CharField(max_length=50,blank=False,default="Test")
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Video(models.Model):
	course = models.ForeignKey(Course,on_delete=models.CASCADE,default=None)
	title = models.CharField(max_length=100,blank=False)
	video = models.FileField(upload_to='media/teachers/videos')	

	def __str__(self):
		return self.title