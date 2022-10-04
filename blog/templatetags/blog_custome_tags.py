from django import template
from blog.models import Post
from blog.models import Category
register = template.Library()

@register.simple_tag()
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


@register.inclusion_tag('blog/blog-latest-posts.html', name='latest')
def latest_posts():
    posts = Post.objects.filter(status=1).order_by('-published_data')[:3]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-category.html', name='category')
def post_categories():    
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = dict()
    for item in categories:
        cat_dict[item] = posts.filter(category=item).count()
    return {'categories': cat_dict}
