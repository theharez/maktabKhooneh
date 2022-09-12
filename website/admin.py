from django.contrib import admin
from website.models import Contact

class Contact_Admin(admin.ModelAdmin):
    
    date_hierarchy = 'created_date'
    list_display = ('name', 'subject', 'created_date')
    list_filter = ('email',)
    search_fields = ['name', 'email']

# Register your models here.
admin.site.register(Contact, Contact_Admin)
