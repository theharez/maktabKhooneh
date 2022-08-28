from unicodedata import name
from django.shortcuts import render

def blog_home_view(request):
    return render(request, 'blog/blog-home.html')

def blog_single_view(request):
    return render(request, 'blog/blog-single.html')