from django.shortcuts import render
from .models import HostGroup

def mainpage(request):
    return render(request, 'mainpage.html')

def index(request):
    return render(request, 'index.html')

def addhosts(request):
    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})
