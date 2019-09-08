from django.shortcuts import render
from .models import Group, Module, Host
from .adhoc2 import adhoc

# Create your views here.

def index(request):
    return render(request, 'webadmin/webadin_index.html')

def add_hosts(request):
    if request.method == 'POST':
        groupname = request.POST.get('group').strip()
        hostname = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if groupname:  # 如果组名非空
            # get_or_create是取出或创建组，返回元组(实例，状态)
            g = Group.objects.get_or_create(groupname=groupname)[0]
            if hostname and ip:  # 如果主机名和ip地址都是非空
                g.host_set.get_or_create(hostname=hostname, ipaddr=ip)

    groups = Group.objects.all()
    return render(request, 'webadmin/add_hosts.html', {'groups': groups})

def add_modules(request):
    if request.method == 'POST':
        modlue_name = request.POST.get('module').strip()
        param = request.POST.get('param').strip()
        if modlue_name:
            m = Module.objects.get_or_create(modulename=modlue_name)[0]
            if param:
                m.arg_set.get_or_create(arg_text=param)

    modules = Module.objects.all()
    return render(request, 'webadmin/add_modules.html', {'modules': modules})

def tasks(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')
        group = request.POST.get('group')
        module = request.POST.get('module')
        arg = request.POST.get('arg')
        if group: # 如果组是非空，则在组上执行任务
            dest = group
        elif ip:  # 如果组为空，主机非空
            dest = ip
        else:
            dest = None

        if dest:  # 如果dest不是None
            if module and arg:  # 如果模块和参数都选择了
                adhoc(['ansi_cfg/dhosts.py'], dest, module, arg)

    groups = Group.objects.all()
    hosts = Host.objects.all()
    modules = Module.objects.all()
    context = {'groups': groups, 'hosts': hosts, 'modules': modules}
    return render(request, 'webadmin/tasks.html', context)

