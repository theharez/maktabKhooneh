from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag
def say_hi():
    return 'Hi budy'

@register.simple_tag(name='plus_self')
def sum(NO):
    return NO + NO

@register.simple_tag(name='post_count')
def func():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='posts')
def func():
    posts = Post.objects.filter(status=1)
    return posts

@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts():
    posts = Post.objects.filter(status=1).order_by('-views')[:2]
    return {'posts': posts}