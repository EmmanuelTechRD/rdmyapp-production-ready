from django.shortcuts import render
from . import models as m

def blog_home(request):
    
    posts = m.Post.objects.order_by('-published_date')
    return render(request, 'blog/posts.html', {'posts': posts,})