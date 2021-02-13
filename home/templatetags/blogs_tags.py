from django import template
from ..models import Blog,Categories
from django.db.models import Count

register = template.Library()

@register.simple_tag
def top_posts(num=3):
    return Blog.published.annotate(total_comments=Count('comments')).order_by('-total_comments','-created')[:num]

@register.simple_tag
def categories():
    return Blog.published.order_by().values('categories__title','categories__slug').annotate(Count('categories__title'))

@register.simple_tag
def tags():
    published = Blog.published.order_by().values('tags__name','tags__slug').distinct()
    return published