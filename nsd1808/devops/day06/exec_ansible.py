import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
# 此处的options选项，实际上就是执行ansible命令时的选项：ansible --help
# connection是连接类型，可以用local/ssh/smart
# module_path指向额外的模块目录
# forks指定创建多个子进程
# become指定切换身份, become_method指定切换方法，become_user指定切换成哪个用户
# check指的是预测命令的执行结果，但是不真正的执行操作
# diff当改变文件、模板，指出改变前后的区别
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# initialize needed objects
# DataLoader负责查找和读取yaml、json和ini文件
loader = DataLoader()  # Takes care of finding and reading yaml, json and ini files
passwords = dict()   # 密码字典


# create inventory, use path to host config file as source or hosts in a comma separated string
# 主机清单，指的是ansible可以管理哪些主机。这些主机，可以用逗号隔开
# 也可以指定主机清单文件列表
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])

# variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
# 变量管理器
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
play_source =  dict(
        name = "Ansible Play",  # 定义paly的名字
        hosts = 'webservers',    # 指定在哪些主机上执行命令
        gather_facts = 'no',    # 不收集主机信息
        tasks = [   # 执行命令
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
# 创建Play的实例
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
tqm = None   # 创建任务队列管理器，执行任务
try:
    tqm = TaskQueueManager(
              inventory=inventory,
              variable_manager=variable_manager,
              loader=loader,
              options=options,
              passwords=passwords,
          )
    result = tqm.run(play) # most interesting data for a play is actually sent to the callback's methods
finally:
    # we always need to cleanup child procs and the structres we use to communicate with them
    if tqm is not None:
        tqm.cleanup()

    # Remove ansible tmpdir  删除临时目录
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
