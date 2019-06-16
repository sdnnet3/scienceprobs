from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Topic(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	slug = models.SlugField(null=True, blank=True, default='')
	content_1 = models.TextField(null=True, blank=True, default='')
	image_1 = models.ImageField(default='default.jpg', upload_to='genchem')
	mnemonic = models.TextField(null=True, blank=True, default='')
	mnemonic_image = models.ImageField(default='default.jpg', upload_to='genchem')
	content_3 = models.TextField(null=True, blank=True, default='')
	image_3 = models.ImageField(default='default.jpg', upload_to='genchem')


	def __str__(self): 
		return self.title

	def get_absolute_url(self):
		return reverse("tutorials:chemDetail", kwargs={"slug": self.slug})
