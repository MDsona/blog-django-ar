from django import template                             # -12a
from blog.models import Post, Comment

register = template.Library()

@register.inclusion_tag('blog/latest_posts.html')       # -12a
def latest_posts():                                     
    context = {
        'l_posts': Post.objects.all()[0:5]
    }
    return context


@register.inclusion_tag('blog/latest_comments.html')       # -13a
def latest_comments():                                     
    context = {
        'l_comments': Comment.objects.filter(active=True)[0:5]
    }

    return context