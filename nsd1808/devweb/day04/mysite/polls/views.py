from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('<h1>投票首页</h1>')
