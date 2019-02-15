from django.shortcuts import render, redirect
from .models import HostGroup, Module, Argument

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

def addmodules(request):
    if request.method == 'POST':
        module = request.POST.get('module').strip()
        arg = request.POST.get('arg').strip()
        if module:
            mod = Module.objects.get_or_create(module_name=module)[0]
            if arg:
                mod.argument_set.get_or_create(argument_text=arg)

    modules = Module.objects.all()
    return render(request, 'addmodules.html', {'modules': modules})

def delarg(request, arg_id):
    argument = Argument.objects.get(id=arg_id)
    argument.delete()
    return redirect('addmodules')

def tasks(request):
    return render(request, 'tasks.html')
