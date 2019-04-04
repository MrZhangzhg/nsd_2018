from django.shortcuts import render
from .models import HostGroup, Module, Host

def index(request):
    return render(request, 'index.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def addhosts(request):
    if request.method == 'POST':
        group_name = request.POST.get('group').strip()
        host = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if group_name:  # 如果group不是空串
            group = HostGroup.objects.get_or_create(group_name=group_name)[0]
            if host and ip:  # 如果host和ip也都不是空串
                group.host_set.get_or_create(hostname=host, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})

def addmodules(request):
    if request.method == 'POST':
        module_name = request.POST.get('module').strip()
        args_text = request.POST.get('params').strip()
        if module_name:
            module = Module.objects.get_or_create(module_name=module_name)[0]
            if args_text:
                module.argument_set.get_or_create(args_text=args_text)

    modules = Module.objects.all()
    return render(request, 'addmodules.html', {'modules': modules})

def tasks(request):
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    hosts = Host.objects.all()
    context = {'groups': groups, 'modules': modules, 'hosts': hosts}

    return render(request, 'tasks.html', context)


