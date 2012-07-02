from django.http import HttpResponseRedirect

from django.contrib.comments import Comment

def comment_posted (request):
    comment = None
    if request.GET['c']:
        try:
            comment = Comment.objects.get(pk=request.GET['c'])
        except Comment.DoesNotExist:
            pass

    if comment:
        return HttpResponseRedirect(comment.get_absolute_url())

    return HttpResponseRedirect('/')
