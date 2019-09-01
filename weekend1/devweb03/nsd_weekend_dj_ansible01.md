# nsd_weekend_dj_ansible01

## ansible/django综合项目

- 通过pycharm创建名为myansible的项目
- 创建用应用

```python
(weekend1) [root@room8pc16 myansible]# python manage.py startapp index
(weekend1) [root@room8pc16 myansible]# python manage.py startapp webadmin
```

- 修改配置文件

```shell
# myansible/settings.py
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    ... ...
    'index',
    'webadmin',
]
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False
# 指定项目的根目录下的static目录是静态文件存储目录
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

- 生成数据库

```shell
(weekend1) [root@room8pc16 myansible]# python manage.py makemigrations
(weekend1) [root@room8pc16 myansible]# python manage.py migrate
# sqlite基本使用方法
(weekend1) [root@room8pc16 myansible]# sqlite3 db.sqlite3 
sqlite> .help   # 查帮助
sqlite> .tables   # 相当于show tables
sqlite> .schema auth_user   # 相当于desc auth_user
sqlite> select * from auth_user;   # sql语句最后也要有分号
```

- 创建管理员

```shell
(weekend1) [root@room8pc16 myansible]# python manage.py createsuperuser
```

- 把投票应用中的static目录拷贝到当前项目的根目录下

```shell
(weekend1) [root@room8pc16 myansible]# cp -r ../mysite/polls/static/ .
```

- 创建模板目录，并把投票应用的base.html拷贝过来

```shell
(weekend1) [root@room8pc16 myansible]# mkdir templates/{index,webadmin} 
(weekend1) [root@room8pc16 myansible]# cp ../mysite/templates/base.html templates/
(weekend1) [root@room8pc16 myansible]# ls templates/
base.html  index  webadmin
```

- 授权，将应用的url交给应用处理

```python
# myansible/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^webadmin/', include('webadmin.urls')),
    # 注意，r''可以匹配任意url
    url(r'', include('index.urls')),
]

# index/urls.py,  webadmin/urls.py
from django.conf.urls import url

urlpatterns = [
]
```

### 编写首页应用

```python
# 1. index/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.index, name='index'),
]

# 2. index/views.py
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index/index.html')

# 3. templates/index/index.html
{% extends 'base.html' %}
{% load static %}
{% block title %}Ansible Webadmin{% endblock %}
{% block content %}
    <div class="row h4">
        <div class="col-sm-3 text-center">
            <a href="">
                <img src="{% static 'imgs/linux.jpg' %}" width="150px"><br>
                主机信息
            </a>
        </div>
        <div class="col-sm-3 text-center">
            <a href="">
                <img src="{% static 'imgs/linux.jpg' %}" width="150px"><br>
                添加主机
            </a>
        </div>
        <div class="col-sm-3 text-center">
            <a href="">
                <img src="{% static 'imgs/linux.jpg' %}" width="150px"><br>
                添加模块
            </a>
        </div>
        <div class="col-sm-3 text-center">
            <a href="">
                <img src="{% static 'imgs/linux.jpg' %}" width="150px"><br>
                执行任务
            </a>
        </div>
    </div>

{% endblock %}
```

## 编写webadmin应用

- 编写数据模型

```python
# webadmin/models.py
from django.db import models

# Create your models here.

class Group(models.Model):
    groupname = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.groupname

class Host(models.Model):
    hostname = models.CharField(max_length=50, unique=True)
    ipaddr = models.CharField(max_length=15)
    group = models.ForeignKey(Group)
    
    def __str__(self):
        return "%s: %s=>%s" % (self.group, self.hostname, self.ipaddr)

class Module(models.Model):
    modulename = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.modulename

class Arg(models.Model):
    arg_text = models.CharField(max_length=100)
    module = models.ForeignKey(Module)
    
    def __str__(self):
        return "%s: %s" % (self.module, self.arg_text)
```

- 生成表

```python
(weekend1) [root@room8pc16 myansible]# python manage.py makemigrations
(weekend1) [root@room8pc16 myansible]# python manage.py migrate
```

- 将模型注册到后台

```python
# webadmin/admin.py
from django.contrib import admin
from .models import Group, Host, Module, Arg

# Register your models here.
for item in [Group, Host, Module, Arg]:
    admin.site.register(item)

# 访问http://x.x.x.x/admin，查看
```









