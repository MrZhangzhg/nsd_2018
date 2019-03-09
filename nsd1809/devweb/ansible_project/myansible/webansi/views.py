from django.shortcuts import render
from .models import HostGroup, Module, Host
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

def adhoc_cmd(sources=None, hosts=None, module=None, args=None):
    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
    loader = DataLoader()
    passwords = dict()
    inventory = InventoryManager(loader=loader, sources=sources)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = dict(
            name="My Ansible Task Test",
            hosts=hosts,
            gather_facts='no',
            tasks=[
                dict(action=dict(module=module, args=args), register='shell_out'),
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
    if request.method == 'POST':
        ip = request.POST.get('ip')
        group_name = request.POST.get('group_name')
        if ip:
            dest = ip
        else:
            dest = group_name
        module_name = request.POST.get('module_name')
        args = request.POST.get('args')
        adhoc_cmd(
            sources=['ansi_cfg/dhosts.py'],
            hosts=dest,
            module=module_name,
            args=args
        )

    groups = HostGroup.objects.all()
    hosts = Host.objects.all()
    modules = Module.objects.all()
    context = {'groups': groups, 'hosts': hosts, 'modules': modules}
    return render(request, 'tasks.html', context)
