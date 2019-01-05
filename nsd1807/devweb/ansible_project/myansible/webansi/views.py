from django.shortcuts import render
from .models import HostGroup, Module, Host
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C
import shutil

def exec_task(servers, hostfile=['ansicfg/gethosts.py'], mod=None, args=None):
    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='smart', module_path=[], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
    loader = DataLoader()
    passwords = dict()
    inventory = InventoryManager(loader=loader, sources=hostfile)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = dict(
        name="My Ansible Play Test",
        hosts=servers,
        gather_facts='no',
        tasks=[
            dict(action=dict(module=mod, args=args), register='shell_out'),
         ]
    )
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
    tqm = None
    try:
        tqm = TaskQueueManager(
                  inventory=inventory,
                  variable_manager=variable_manager,
                  loader=loader,
                  options=options,
                  passwords=passwords,
              )
        result = tqm.run(play)
    finally:
        if tqm is not None:
            tqm.cleanup()
        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

def index(request):
    return render(request, 'index.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def addhosts(request):
    if request.method == 'POST':
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        group = request.POST.get('group')
        if group:
            # get_or_create返回元组(实例, 0/1)
            hostgroup = HostGroup.objects.get_or_create(groupname=group)[0]
            if hostname and ip:
                hostgroup.host_set.get_or_create(hostname=hostname, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})

def addmodules(request):
    if request.method == 'POST':
        module = request.POST.get('module')
        argument = request.POST.get('argument')
        if module:
            mod = Module.objects.get_or_create(module_name=module)[0]
            if argument:
                mod.argument_set.get_or_create(argument_text=argument)

    modules = Module.objects.all()
    return render(request, 'addmodules.html', {'modules': modules})

def tasks(request):
    if request.method == 'POST':
        host = request.POST.get('server')
        group = request.POST.get('hostgroup')
        module = request.POST.get('module')
        args = request.POST.get('argument')
        if host:
            server = host
        else:
            server = group
        exec_task(servers=server, mod=module, args=args)

    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    return render(request, 'tasks.html', {'hosts': hosts, 'groups': groups, 'modules': modules})
