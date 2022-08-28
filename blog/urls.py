from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('', blog_home_view, name='blog_home_view'),
    path('single', blog_single_view, name='blog_single_view')
]
