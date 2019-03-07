from django.shortcuts import render
from .models import Blog

def index(request):
    blogs = Blog.objects.order_by('-pub_date')
    return render(request, 'blog_index.html', {'blogs': blogs})
