from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor

Options = namedtuple(
    'Options',
    [
        'connection',
        'remote_user',
        'ask_sudo_pass',
        'verbosity',
        'ask_pass',
        'module_path',
        'forks',
        'become',
        'become_method',
        'become_user',
        'check',
        'listhosts',
        'listtasks',
        'listtags',
        'syntax',
        'sudo_user',
        'sudo',
        'diff'
    ]
)
options = Options(
    connection='smart',
    remote_user=None,
    ask_pass=None,
    sudo_user=None,
    forks=5,
    sudo=None,
    ask_sudo_pass=False,
    verbosity=5,
    module_path=None,
    become=None,
    become_method=None,
    become_user=None,
    check=False,
    diff=False,
    listhosts=None,
    listtasks=None,
    listtags=None,
    syntax=None
)

def run_pb(sources, pb_path):
    loader = DataLoader()
    passwords = dict()
    inventory = InventoryManager(loader=loader, sources=sources)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    pb = PlaybookExecutor(
        playbooks=pb_path,
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=options,
        passwords=passwords
    )
    result = pb.run()
    return result

if __name__ == '__main__':
    sources = ['myansible/hosts']
    playbook = ['myansible/lamp.yml']
    run_pb(sources, playbook)
