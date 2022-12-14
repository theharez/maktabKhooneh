from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(blank=True, null=True, max_length=11)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return (f'{self.name} /// {self.email}')

class news_letter(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email
