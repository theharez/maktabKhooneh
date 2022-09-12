from multiprocessing import context
from django.shortcuts import render
from blog.models import Post

def blog_home_view(request):
    posts = Post.objects.filter(status=True)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single_view(request):
    return render(request, 'blog/blog-single.html')