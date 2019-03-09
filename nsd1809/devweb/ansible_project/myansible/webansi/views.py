from django.shortcuts import render
from .models import HostGroup

def mainpage(request):
    return render(request, 'mainpage.html')

def index(request):
    return render(request, 'index.html')

def addhosts(request):
    if request.method == 'POST':
        hostname = request.POST.get('hostname').strip()
        ip = request.POST.get('ip').strip()
        group_name = request.POST.get('group').strip()
        if group_name:
            # get_or_create返回元组(组实例, True|False)
            group = HostGroup.objects.get_or_create(group_name=group_name)[0]
            if hostname and ip:
                group.host_set.get_or_create(hostname=hostname, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})
