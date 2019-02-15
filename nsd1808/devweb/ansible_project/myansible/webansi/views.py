from django.shortcuts import render
from .models import HostGroup

def index(request):
    return render(request, 'index.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def addhosts(request):
    if request.method == 'POST':
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        group = request.POST.get('group').strip()
        if group:   # 如果组不为空
            # get_or_create返回元组(实例, True|False)
            hostgroup = HostGroup.objects.get_or_create(group_name=group)[0]
            if host and ip:  # 如果host和ip都不为空
                hostgroup.host_set.get_or_create(hostname=host, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})
