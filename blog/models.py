from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=255)   
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    views = models.IntegerField(default=0)
    tags = TaggableManager()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # or (on_delete=models.SET_NULL)
    category = models.ManyToManyField(Category)
    status = models.BooleanField(default=False)
    need_to_login = models.BooleanField(default=False)
    image = models.ImageField(upload_to='blog/', default='blog/2switch.png')
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    published_data = models.DateTimeField(null=True)    
    class Meta:
        ordering = ['-published_data',]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:blog_single_view', kwargs={'pid': self.id})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-created_date',)
    
    def __str__(self):
        return (f'{self.name} / {self.subject}')