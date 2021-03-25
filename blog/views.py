from django.shortcuts import render
from django.http import Http404
from .models import Blog

def blog(request, slug_value):
    try:
        blog = Blog.objects.get(slug=slug_value)
    except Blog.DoesNotExist:
        raise Http404('Blog not found')
    return render(request,'blog/blog.html')

