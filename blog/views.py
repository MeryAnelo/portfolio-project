import logging
from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog(request, slug_value):
    blog = get_object_or_404(Blog, slug=slug_value)
    logging.info("Blog page was accessed, all blog data: %s", blog)
    return render(request, 'blog/blog.html', {'blog': blog})
