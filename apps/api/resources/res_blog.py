"""
Resources blog
"""
__docformat__ = 'epytext en'

from basic.blog.models import Post
from .common import CommonModelResource



class BlogResource (CommonModelResource):
    class Meta:
        queryset = Post.objects.published()
        fields = ['title', 'tease', 'body', 'publish']
