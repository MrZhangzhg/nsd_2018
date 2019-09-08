# nsd_weekend_dj_ansible02

《django by example》：https://www.jianshu.com/p/05810d38f93a

## 配置ansible工作环境

```shell
(weekend1) [root@room8pc16 myansible]# mkdir ansi_cfg
(weekend1) [root@room8pc16 myansible]# vim ansi_cfg/ansible.cfg
[defaults]
inventory = dhosts.py
remote_user = root

# 创建动态主机清单文件，将主机和组从数据库中取出
(weekend1) [root@room8pc16 myansible]# touch ansi_cfg/dhosts.py
(weekend1) [root@room8pc16 myansible]# chmod +x ansi_cfg/dhosts.py
# dhosts.py输出格式要求如下
{
	"组1": {"hosts": ["主机1", "主机2"]},
	"组2": {"hosts": ["主机3", "主机4"]},
}
(weekend1) [root@room8pc16 myansible]# vim ansi_cfg/dhosts.py
#!/root/weekend1/bin/python

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "sqlite:////var/ftp/nsd_2018/weekend1/myansible/db.sqlite3",
    encoding='utf8'
)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Group(Base):
    __tablename__ = 'webadmin_group'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(50), unique=True)

class Host(Base):
    __tablename__ = 'webadmin_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50), unique=True)
    ipaddr = Column(String(15))
    group_id = Column(Integer, ForeignKey('webadmin_group.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(Group.groupname, Host.ipaddr).join(Host)
    # print(qset.all())
    result = {}
    for group, ip in qset:
        if group not in result:
            result[group] = {}
            result[group]['hosts'] = []
        result[group]['hosts'].append(ip)

    print(result)

```

## 制作主机信息页

```shell
# 收集所有主机的信息
(weekend1) [root@room8pc16 ansi_cfg]# ansible all -m setup --tree /tmp/out
# 将收集到的信息生成web页面
(weekend1) [root@room8pc16 ansi_cfg]# ansible-cmdb /tmp/out > ../templates/webadmin/webadmin_index.html
# 修改url
# webadmin/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='webadmin_index'),
]
# 创建函数
# webadmin/views.py
def index(request):
    return render(request, 'webadmin/webadin_index.html')
# 修改index.html，添加超链接
# templates/index/index.html
<a href="{% url 'webadmin_index' %}" target="_blank">
    <img src="{% static 'imgs/linux.jpg' %}" width="150px"><br>
    主机信息
</a>
```

## 制作添加主机页

```python
# webadmin/urls.py
    url(r'^addhosts/$', views.add_hosts, name='add_hosts'),

# webadmin/views.py
def add_hosts(request):
    if request.method == 'POST':
        groupname = request.POST.get('group').strip()
        hostname = request.POST.get('host').strip()
        ip = request.POST.get('ip').strip()
        if groupname:  # 如果组名非空
            g = Group.objects.get_or_create(groupname=groupname)[0]
            if hostname and ip:  # 如果主机名和ip地址都是非空
                g.host_set.get_or_create(hostname=hostname, ipaddr=ip)

    groups = Group.objects.all()
    return render(request, 'webadmin/add_hosts.html', {'groups': groups})


# templates/webadmin/add_hosts.html
{% extends 'base.html' %}
{% load static %}
{% block title %}添加主机{% endblock %}
{% block content %}
    <form action="" method="post" class="form-inline h4">
        {% csrf_token %}
        <div class="form-group">
            <label>主机组：</label>
            <input type="text" class="form-control" name="group">
        </div>
        <div class="form-group">
            <label>主机：</label>
            <input type="text" class="form-control" name="host">
        </div>
        <div class="form-group">
            <label>IP地址：</label>
            <input type="text" class="form-control" name="ip">
        </div>
        <div class="form-group">
            <input type="submit" class="btn btn-primary" value="提 交">
        </div>
    </form>
    <hr>
    <table class="table table-hover table-striped h4">
        <thead class="bg-primary">
            <tr>
                <td>主机组</td>
                <td>主机</td>
            </tr>
        </thead>
        {% for group in groups %}
            <tr>
                <td>{{ group.groupname }}</td>
                <td>
                    <ul class="list-unstyled">
                        {% for host in group.host_set.all %}
                            <li>
                                {{ host.hostname }}: {{ host.ipaddr }}
                            </li>
                        {% endfor %}
                    </ul>
                </td>
            </tr>
        {% endfor %}
    </table>
{% endblock %}

# 修改templates/index/index.html超链接
    <a href="{% url 'add_hosts' %}" target="_blank">

```

## 制作添加模块页

```python
# webadmin/urls.py
	url(r'^addmodules/$', views.add_modules, name='add_modules'),

# webadmin/views.py
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

# templates/webadmin/add_modules.html
{% extends 'base.html' %}
{% load static %}
{% block title %}添加模块{% endblock %}
{% block content %}
    <form action="" method="post" class="form-inline h4">
        {% csrf_token %}
        <div class="form-group">
            <label>模块：</label>
            <input type="text" class="form-control" name="module">
        </div>
        <div class="form-group">
            <label>参数：</label>
            <input type="text" class="form-control" name="param">
        </div>
        <div class="form-group">
            <input type="submit" class="btn btn-primary" value="提 交">
        </div>
    </form>
    <hr>
    <table class="table table-hover table-striped h4">
        <thead class="bg-primary">
            <tr>
                <td>模块</td>
                <td>参数</td>
            </tr>
        </thead>
        {% for module in modules %}
            <tr>
                <td>{{ module.modulename }}</td>
                <td>
                    <ul class="list-unstyled">
                        {% for arg in module.arg_set.all %}
                            <li>
                                {{ arg.arg_text }}
                            </li>
                        {% endfor %}
                    </ul>
                </td>
            </tr>
        {% endfor %}
    </table>
{% endblock %}

# 修改 templates/index/index.html中的超链接
	<a href="{% url 'add_modules' %}" target="_blank">

```

## 制作执行任务页面

```python
# webadmin/urls.py
    url(r'^tasks/$', views.tasks, name='tasks'),

# 将ansible课程中adhoc2.py拷贝到webadmin目录下
    
# webadmin/veiws.py
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



# templates/webadmin/tasks.html
{% extends 'base.html' %}
{% load static %}
{% block title %}执行任务{% endblock %}
{% block content %}
    <form action="" method="post" class="h4">
        {% csrf_token %}
        <ul class="nav nav-tabs">
            <li class="active"><a href="#server" data-toggle="tab">主机</a></li>
            <li><a href="#servergroup" data-toggle="tab">主机组</a></li>
        </ul>
        <div class="tab-content" style="margin: 5px 0">
            <div id="server" class="tab-pane active fade in">
                <select class="form-control" name="ip">
                    <option value="">无</option>
                    {% for host in hosts %}
                        <option value="{{ host.ipaddr }}">{{ host.hostname }}</option>
                    {% endfor %}
                </select>
            </div>
            <div id="servergroup" class="tab-pane fade">
                <select class="form-control" name="group">
                    <option value="">无</option>
                    {% for group in groups %}
                        <option value="{{ group.groupname }}">{{ group.groupname }}</option>
                    {% endfor %}
                </select>
            </div>
        </div>
        <table class="table table-hover table-bordered table-striped">
            <thead class="bg-primary">
                <tr>
                    <td>模块</td>
                    <td>参数</td>
                </tr>
            </thead>
            {% for module in modules %}
                <tr>
                    <td>
                        <div class="radio">
                            <label>
                                <input type="radio" name="module" value="{{ module.modulename }}">
                                {{ module.modulename }}
                            </label>
                        </div>
                    </td>
                    <td>
                        {% for arg in module.arg_set.all %}
                            <div class="radio">
                                <label>
                                    <input type="radio" name="arg" value="{{ arg.arg_text}}">
                                    {{ arg.arg_text }}
                                </label>
                            </div>
                        {% endfor %}
                    </td>
                </tr>
            {% endfor %}
        </table>
    <div class="form-group text-center">
        <input class="btn btn-primary" type="submit" value="执 行">
    </div>
    </form>
{% endblock %}

# 修改templates/index/index.html中的超链接
	<a href="{% url 'tasks' %}" target="_blank">

```













