from django.shortcuts import render, redirect
from .models import HostGroup, Module, Host, Argument
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

def ad_hoc(inventory_fname, hosts, module, args):
    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='ssh', module_path=[''], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
    loader = DataLoader()
    passwords = dict()
    inventory = InventoryManager(loader=loader, sources=inventory_fname)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source=dict(
            name="my ansible play",
            hosts=hosts,
            gather_facts='no',
            tasks=[
                dict(action=dict(module=module, args=args), register='shell_out'),
                # dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
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
    if request.method == 'POST':
        ip = request.POST.get('host')
        group_name = request.POST.get('group')
        module_name = request.POST.get('module')
        args_text = request.POST.get('params')
        # 如果组名不是空的就在组上执行任务，否则在主机上执行任务
        if group_name:
            dest = group_name
        else:
            dest = ip

        ad_hoc(['ansi_cfg/dhosts.py'], dest, module_name, args_text)

    groups = HostGroup.objects.all()
    modules = Module.objects.all()
    hosts = Host.objects.all()
    context = {'groups': groups, 'modules': modules, 'hosts': hosts}
    return render(request, 'tasks.html', context)

def delargs(request, args_id):
    argument = Argument.objects.get(id=args_id)
    argument.delete()
    return redirect('addmodules')
