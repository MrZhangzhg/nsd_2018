import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
# 通过命名的元组，定义ansible临时命令的选项
# connection：连接类型，有local(在本机执行命令)、ssh、smart(智能)
# module_path: 指定自定义模块的路径
# forks: 创建子进程的数目
# become: 是否切换成其他用户，比如通过普通用户连接远程主机，执行任务的时候切换成管理员
# check: 只是预测执行命令后在远程主机上将会产生什么样的影响，不会真正地执行命令
# diff: 当改变文件和模板时，显示改变了哪些内容
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# initialize needed objects
# Dataloader负责查找、读取yaml/json/ini文件，分析它们的结构，转换成python的数据类型
loader = DataLoader()  # Takes care of finding and reading yaml, json and ini files
# passwords用于存储各类密码，免密方式，密码为空即可
passwords = dict()

# create inventory, use path to host config file as source or hosts in a comma separated string
# inventory: 主机清单文件，列出ansible管理的机器有哪些
# 表示方式，可以用逗号把所有的主机分隔开，也可以使用主机清单文件列表
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources=['mykvm/hosts'])

# variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
# variable_mananger: 用于分析ansible变量
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
# 定义执行任务的相关信息
play_source = dict(
        name="My Ansible Task Test",
        hosts='webservers',  # 定义在哪些主机上执行任务
        gather_facts='no',   # 不收集主机信息
        tasks=[
            dict(action=dict(module='shell', args='id root'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
# 创建play实例
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
# 创建任务队列管理器的实例
tqm = None
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

    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
