from django.shortcuts import render

def mainpage(request):
    return render(request, 'mainpage.html')

def index(request):
    return render(request, 'index.html')
