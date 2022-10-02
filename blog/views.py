from django.shortcuts import render, get_object_or_404, get_list_or_404
from blog.models import Post
from django.utils import timezone

def blog_home_view(request, **kwargs):    
    posts = Post.objects.filter(published_data__lte=timezone.now(), status=True)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_name') != None:
        posts = posts.filter(author__username=kwargs['author_name'])
    context = {'posts': posts} 
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request, pid):
    single = get_object_or_404(Post, id=pid, status=True, published_data__lte=timezone.now())
    single.views +=1 
    single.save()
    context = {'single': single}
    try:
        next = get_list_or_404(Post, id__gt=single.id, published_data__lte=timezone.now(), status=True)
        context.update({'single': single, 'next':next[0]})
    except:
        context = {'single': single}
    try:
        prev = get_list_or_404(Post, id__lt=single.id, published_data__lte=timezone.now(), status=True)
        context.update({'single': single, 'prev':prev[-1]})
    except:
        context.update({'single': single})
    return render(request, 'blog/blog-single.html', context)

def blog_search(request):
    posts = Post.objects.filter(published_data__lte=timezone.now(), status=True)
    if request.method == 'GET':
        if search := request.GET.get('search'):
            posts = posts.filter(content__contains=search)
    context = {'posts': posts} 
    return render(request, 'blog/blog-home.html', context)


def test(request):
    return render(request, 'test.html')