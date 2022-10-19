from django.contrib import admin
from blog.models import Post, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class Post_Admin(SummernoteModelAdmin):
    
    date_hierarchy = 'created_data' # posts based on created_data or other DateTimeField 
    empty_value_display = '-'   # unpublished posts
    list_display = ('id','title', 'author', 'status', 'created_data', 'views', 'published_data')   # columns to show 
    list_filter = ('status', 'author')  # acsending or deseding sorting
    # ordering = ('created_data',)    # ordering by
    search_fields = ['title', 'content']    # looking for an expression in the title or the content
    summernote_fields = '__all__'
    
admin.site.register(Post, Post_Admin)
admin.site.register(Category)
