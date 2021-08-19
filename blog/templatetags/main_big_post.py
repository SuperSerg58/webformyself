from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/main_big_post.html')
def main_post():
    post = Post.objects.latest('id')
    return {"post": post}
