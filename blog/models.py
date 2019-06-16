from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model): 
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    title = models.CharField(max_length=200) 
    content = models.TextField()
    clip = models.TextField(default='')
    featureImage = models.ImageField(default='default.jpg', upload_to='blog')
    #publish date and slug are both used in ref url generation 
    #look into designing a highlights method that only shows highlights for 
    #recently published articles plus a few weeks?
    created_date = models.DateTimeField(default=timezone.now) 
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(default=None)

    #highlight lets it show up in sidebar
    highlight = models.BooleanField(default = False)

    def publish(self): 
        self.published_date = timezone.now() 
        self.save() 

    def __str__(self): 
        return self.title

    def snippet(self):
        return self.clip

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug':self.slug})

class Note(models.Model):
    title = models.CharField(max_length = 100, default = None)
    text = models.TextField(default = None)
    slug = models.SlugField(default = None)
    notenumber = models.IntegerField(default = 1)

    def __str__(self):
        return self.title