from django.shortcuts import render
from .models import HostGroup, Module

def index(request):
    return render(request, 'index.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def addhosts(request):
    if request.method == 'POST':
        groupname = request.POST.get('group').strip()
        hostname = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if groupname:
            # get_or_create返回的是元组(组实例, True|False)
            group = HostGroup.objects.get_or_create(groupname=groupname)[0]
            if hostname and ip:
                group.host_set.get_or_create(hostname=hostname, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})

def addmodules(request):
    modules = Module.objects.all()
    return render(request, 'addmodules.html', {'modules': modules})
