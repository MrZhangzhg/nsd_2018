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
if __name__ == '__main__':
    sources = ['mykvm/hosts']
    hosts = 'webservers'
    module = 'yum'
    args = 'name=php state=latest'
    adhoc_cmd(sources, hosts, module, args)
