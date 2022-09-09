from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    published_data = models.DateTimeField(null=True)
    
    class Meta:
        ordering = ['status']

    def __str__(self):
        return self.title