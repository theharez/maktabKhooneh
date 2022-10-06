from django import template
from blog.models import Post
from blog.models import Category
from django.utils import timezone
register = template.Library()

@register.inclusion_tag('main_page/index-latest-posts.html')
def website_latest_posts():
    posts = Post.objects.filter(published_data__lte=timezone.now(), status=True)
    return {'posts': posts}