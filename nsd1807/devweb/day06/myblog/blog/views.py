from django.shortcuts import render, HttpResponse
from .models import Blog

def index(request):
    articles = Blog.objects.order_by('-pub_date')
    return render(request, 'index.html', {'articles': articles})

def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')

def welcome(request, name):
    return HttpResponse('<h1>Hi %s</h1>' % name)
