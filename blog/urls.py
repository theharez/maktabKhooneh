from django.urls import path
from blog.views import *

from blog.rss import LatestEntriesFeed

app_name = 'blog'
urlpatterns = [
    path('', blog_home_view, name='blog_home_view'),
    path('<int:pid>', blog_single_view, name='blog_single_view'),
    path('categor/<str:cat_name>', blog_home_view, name='category'),
    path('tag/<str:tag_name>', blog_home_view, name='tag'),
    path('author/<str:author_name>', blog_home_view, name='author'),
    path('search/', blog_search, name='search'),
    path('rss/feed', LatestEntriesFeed()),
    path('test', test, name='test')   
]
