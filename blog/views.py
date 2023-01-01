from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, InvalidPage
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse


def blog_home_view(request, **kwargs):    
    posts = Post.objects.filter(published_data__lte=timezone.now(), status=True)
    
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_name') != None:
        posts = posts.filter(author__username=kwargs['author_name'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
        
    posts = Paginator(posts, 3)
    page_number = request.GET.get('page')

    try:
        posts = posts.page(page_number)
    except (InvalidPage):
        posts = posts.page(1)
        
    context = {'posts': posts} 
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request, pid):
    single = get_object_or_404(Post, id=pid, status=True, published_data__lte=timezone.now())
    if single.need_to_login and not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        single.views +=1 
        single.save()
        
        form = CommentForm()
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                messages.add_message(request, messages.SUCCESS, 'Your comment has been submitted')
                form.save()
            else:
                messages.add_message(request, messages.ERROR, "Your comment has not been submitted")
                
        comments = Comment.objects.filter(post=pid, approved=True)
        context = {'single': single, 'comments': comments, 'form':form}
        
        try:
            next = get_list_or_404(Post, id__gt=single.id, published_data__lte=timezone.now(), status=True)
            context.update({'next':next[0]})
        except:
            pass    
        try:
            prev = get_list_or_404(Post, id__lt=single.id, published_data__lte=timezone.now(), status=True)
            context.update({'prev':prev[-1]})
        except:
            pass
            
        return render(request, 'blog/blog-single.html', context)


def blog_search(request):
    posts = Post.objects.filter(published_data__lte=timezone.now(), status=True)
    if request.method == 'GET':
        if request.GET.get('search'):
            search = request.GET.get('search')
            posts = posts.filter(content__contains=search)
    context = {'posts': posts} 
    return render(request, 'blog/blog-home.html', context)


def test(request):
    return render(request, 'test.html')