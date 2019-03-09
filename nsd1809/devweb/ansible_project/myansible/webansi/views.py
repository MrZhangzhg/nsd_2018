from django.shortcuts import render
from .models import HostGroup, Module, Host

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

def addmodules(request):
    if request.method == 'POST':
        module_name = request.POST.get('module').strip()
        args = request.POST.get('args').strip()
        if module_name:
            module = Module.objects.get_or_create(modlue_name=module_name)[0]
            if args:
                module.argument_set.get_or_create(arg_text=args)

    modules = Module.objects.all()
    return render(request, 'addmodules.html', {'modules': modules})

def tasks(request):
    groups = HostGroup.objects.all()
    hosts = Host.objects.all()
    modules = Module.objects.all()
    context = {'groups': groups, 'hosts': hosts, 'modules': modules}
    return render(request, 'tasks.html', context)
