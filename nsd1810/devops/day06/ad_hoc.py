import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
# 这里只是定义执行ansible时的选项，参见ansible --help
# connection: 连接的类型，有local(本机执行)/ssh(通过ssh执行)/smart(智能选择)
# module_path: 自定义的模块路径
# forks: 并行执行程序的进程数
# become相关：建议使用普通用户连接远程服务器，执行操作的时候再切换成root，become指定切换成哪个用户，切换的方法是什么
# check: 不真正的执行命令，而是预言将会发生什么
# diff: 当改变文件或模板时，指出修改了什么
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# initialize needed objects
# loader: 负责查找和读取yaml、json和ini文件，能够在文件中取出正确的数据
loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
# 存储各种各样的密码
passwords = dict()

# create inventory, use path to host config file as source or hosts in a comma separated string
# 定义主机清单，可以采用两种方式：
# sources='用逗号分开的所有的主机'
# sources=[主机清单文件]
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])

# variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
# 定义变量管理器
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
# 创建要执行的play源
play_source=dict(
        name="my ansible play",
        hosts='webservers',  # 指定在哪些主机上执行任务
        gather_facts='no',  # 不收集主机的信息
        tasks=[  # 定义在主机上执行的任务
            dict(action=dict(module='shell', args='ls -ld /home'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
# 创建play实例
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
    # 清理任务
    if tqm is not None:
        tqm.cleanup()

    # Remove ansible tmpdir
    # 删除临时目录
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
