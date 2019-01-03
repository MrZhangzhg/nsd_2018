from django.shortcuts import render, HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')

def welcome(request, name):
    return HttpResponse('<h1>Hi %s</h1>' % name)
