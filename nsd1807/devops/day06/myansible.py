import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# ansible命令的选项
# connection的值可以是local表示本地，也可以是ssh，还可以是smart
# module_path可以指定额外的自定义模块路径
# forks指定创建多少子进程并行执行命令
# check不在目标主机上真正执行命令，只是预测出现什么结果
# diff当修改文件时，显示有哪些改动
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# initialize needed objects
# 初始化所需要的对象
# DataLoader用于分析yaml/json/ini格式的文件
loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
# 用于存储各种各样的密码
# passwords = dict(vault_pass='secret')
passwords = dict()

# create inventory, use path to host config file as source or hosts in a comma separated string
# 创建主机清单，sources可以是用逗号隔开的所有的主机，也可以用主机清单文件列表
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources=['myansi/hosts'])

# variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
# 变量管理器
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
# 创建Play结构
play_source = dict(
        name="My Ansible Play Test",   # Play的名字
        hosts='webservers',  # 在哪些主机上执行任务
        gather_facts='no',   # 不收集主机信息
        tasks=[   # 要执行的命令
            dict(action=dict(module='shell', args='mkdir /tmp/abcd'), register='shell_out'),
            # dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
# 实例化一个Play对象
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
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
    # 清理子进程
    if tqm is not None:
        tqm.cleanup()

    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
