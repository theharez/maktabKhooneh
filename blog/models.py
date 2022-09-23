
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # or (on_delete=models.SET_NULL)
    category = models.ManyToManyField(Category)
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='blog/', default='blog/2switch.png')
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    published_data = models.DateTimeField(null=True)
    
    class Meta:
        ordering = ['status',]

    def __str__(self):
        return self.title