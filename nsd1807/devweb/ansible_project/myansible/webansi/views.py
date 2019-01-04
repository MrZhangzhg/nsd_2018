from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('<h1>Success</h1>')
