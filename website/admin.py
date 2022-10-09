from django.contrib import admin
from website.models import Contact, news_letter
from django.db import models
from django.forms import Textarea

class Contact_Admin(admin.ModelAdmin):
    
    date_hierarchy = 'created_date'
    list_display = ('name', 'subject', 'email', 'phone', 'created_date')
    list_filter = ('email',)
    search_fields = ['name', 'email']
    formfield_overrides = { models.SmallIntegerField: {'widget': Textarea(attrs={'rows':1, 'cols':20})}}

# Register your models here.
admin.site.register(Contact, Contact_Admin)
admin.site.register(news_letter)
