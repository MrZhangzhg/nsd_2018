# nsd_weekend_devweb03

## python shell

```python
(weekend1) [root@room8pc16 mysite]# python manage.py shell
>>> from polls.models import Question, Choice
# django为每一个模型都创建了名为objects的管理器，对模型的CRUD操作都可以通过这个管理器实现
# 创建问题方法一：实例化
>>> q1 = Question(question_text='你买到放假回家的票了吗？', pub_date='2019-09-01')
>>> q1.save()

# 创建问题方法二：通过objects管理器
>>> q2 = Question.objects.create(question_text='中秋节买月饼吗？', pub_date='2019-8-30')

# 创建选项方法一：实例化
>>> c1 = Choice(choice_text='买到了', question=q1)
>>> c1.save()

# 创建选项方法二：通过objects管理器
>>> c2 = Choice.objects.create(choice_text='没买到', question=q1)

# 问题Question和选项Choice有一对多的关系，一个问题可以有很多选项。选项的类名是Choice，那么问题的实例就有一个名为choice_set的管理器，可以通过问题来创建选项。
# 方法三：通过问题实例的choice_set管理器创建
>>> c3 = q1.choice_set.create(choice_text='不用买票')

# 修改，只要将实例属性重新赋值
>>> q2.question_text = '中秋节买什么？'
>>> q2.save()

# 删除，直接调用实例方法
>>> q2.delete()

# 查询，get方法要求必须查到一个实例，0或多都会出错
>>> q1 = Question.objects.get(id=1)
>>> q1
<Question: 你期待的工资是多少？>

# 查询，filter方法返回由0到多个实例构成查询集
>>> qset1 = Question.objects.filter(id__lt=10)
>>> qset1
>>> qset1[0]

# 查询条件，django用双下划线来表示属性和方法，而不是句点
>>> Question.objects.filter(id__lte=5)  # 小于等于
>>> Question.objects.filter(id__gt=5)   # 大于5
>>> Question.objects.filter(id__exact=1)  # id=1是它的简写
>>> Question.objects.filter(pub_date__month=9)
>>> Question.objects.filter(question_text__startswith='你期待')

# 排序
>>> Question.objects.all()  # 取出所有问题
>>> Question.objects.order_by('pub_date')  # 升序排列
>>> Question.objects.order_by('-pub_date')  # 降序排列
>>> Question.objects.filter(question_text__startswith='你期待').order_by('-pub_date')
```

## 制作投票首页

```python
# 1. views.py
from django.shortcuts import render
from .models import Question

def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'index.html', {'questions': questions})

# 2. templates/index.html
<body>
<h1>投票首页</h1>
{% for question in questions %}
    <p>
        {{ forloop.counter }}.
        <a href="">
            {{ question.question_text }}
        </a>
        {{ question.pub_date }}
    </p>
{% endfor %}
</body>

# 3. 引入bootstrap到模板
# 将前一天的static目录拷贝到polls目录下
[root@room8pc16 weekend1]# cp -r devweb02/static/ mysite/polls/
# 修改index.html头部
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    ... ...
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
</head>
# 在index.html尾部添加
<body>
... ...
<script src="{% static 'js/jquery.min.js' %}"></script>
<script src="{% static 'js/bootstrap.min.js' %}"></script>
</body>

# 4. 修改index.html，完整如下：
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>投票首页</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
</head>
<body>
<div class="container">
    <div id="linux-carousel" class="carousel slide">
        <ol class="carousel-indicators">
            <li class="active" data-target="#linux-carousel" data-slide-to="0"></li>
            <li data-target="#linux-carousel" data-slide-to="1"></li>
            <li data-target="#linux-carousel" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
            <div class="item active">
                <a href="http://www.sogou.com" target="_blank">
                    <img src="{% static 'imgs/first.jpg' %}">
                </a>
            </div>
            <div class="item">
                <img src="{% static 'imgs/second.jpg' %}">
            </div>
            <div class="item">
                <img src="{% static 'imgs/third.jpg' %}">
            </div>
        </div>
        <a href="#linux-carousel" data-slide="prev" class="carousel-control left">
            <span class="glyphicon glyphicon-chevron-left"></span>
        </a>
        <a href="#linux-carousel" data-slide="next" class="carousel-control right">
            <span class="glyphicon glyphicon-chevron-right"></span>
        </a>
    </div>
    <h1 class="text-center text-warning">投票首页</h1>
    <div class="h4" style="margin-top: 20px">
        {% for question in questions %}
            <p>
                {{ forloop.counter }}.
                <a href="{% url 'detail' question.id %}" target="_blank">
                    {{ question.question_text }}
                </a>
                {{ question.pub_date }}
            </p>
        {% endfor %}
    </div>
    <div class="text-center h4" style="margin-top: 50px">
        达内云计算学院 <a href="">weekend1</a>
    </div>
</div>

<script src="{% static 'js/jquery.min.js' %}"></script>
<script src="{% static 'js/bootstrap.min.js' %}"></script>
<script type="text/javascript">
    $('#linux-carousel').carousel({
        interval : 3000
    });
</script>
</body>
</html>
```

## 模板继承

```python
# 1. 拷贝index.html为base.html
# 2. 在base.html中，把个性化内容移除，用block占位
# base.html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
</head>
<body>
<div class="container">
    <div id="linux-carousel" class="carousel slide">
        <ol class="carousel-indicators">
            <li class="active" data-target="#linux-carousel" data-slide-to="0"></li>
            <li data-target="#linux-carousel" data-slide-to="1"></li>
            <li data-target="#linux-carousel" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
            <div class="item active">
                <a href="http://www.sogou.com" target="_blank">
                    <img src="{% static 'imgs/first.jpg' %}">
                </a>
            </div>
            <div class="item">
                <img src="{% static 'imgs/second.jpg' %}">
            </div>
            <div class="item">
                <img src="{% static 'imgs/third.jpg' %}">
            </div>
        </div>
        <a href="#linux-carousel" data-slide="prev" class="carousel-control left">
            <span class="glyphicon glyphicon-chevron-left"></span>
        </a>
        <a href="#linux-carousel" data-slide="next" class="carousel-control right">
            <span class="glyphicon glyphicon-chevron-right"></span>
        </a>
    </div>
    
    {% block content %}{% endblock %}
    
    <div class="text-center h4" style="margin-top: 50px">
        达内云计算学院 <a href="">weekend1</a>
    </div>
</div>

<script src="{% static 'js/jquery.min.js' %}"></script>
<script src="{% static 'js/bootstrap.min.js' %}"></script>
<script type="text/javascript">
    $('#linux-carousel').carousel({
        interval : 3000
    });
</script>
</body>
</html>
# 3. 修改index.html，把共性内容删除，个性内容发到相应的block中
{% extends 'base.html' %}
{% load static %}
{% block title %}投票首页{% endblock %}
{% block content %}
    <h1 class="text-center text-warning">投票首页</h1>
    <div class="h4" style="margin-top: 20px">
        {% for question in questions %}
            <p>
                {{ forloop.counter }}.
                <a href="{% url 'detail' question.id %}" target="_blank">
                    {{ question.question_text }}
                </a>
                {{ question.pub_date }}
            </p>
        {% endfor %}
    </div>
{% endblock %}
```

## 编写问题详情页

```python
# 1. views.py
def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'detail.html', {'question': question})

# 2. detail.html
{% extends 'base.html' %}
{% load static %}
{% block title %}投票详情页{% endblock %}
{% block content %}
    <h1 class="text-center text-warning">
        {{ question.id }}号问题投票详情
    </h1>
    <h3>{{ question.question_text }}</h3>
    <div class="h4">
        <form action="" method="post">
            {% csrf_token %}
            {% for choice in question.choice_set.all %}
                <div class="radio">
                    <label>
                        <input type="radio" name="choice_id" value="{{ choice.id }}">
                        {{ choice.choice_text }}
                    </label>
                </div>
            {% endfor %}
            <div class="form-group">
                <input class="btn btn-primary" type="submit" value="提 交">
            </div>
        </form>
    </div>
{% endblock %}
```

## 实现投票功能

- 投票功能，就是修改数据库中表的votes字段
- 修改数据库是通过执行函数实现的
- 执行函数是通过访问URL实现的

```python
# 1. 编写投票功能url
# urls.py
urlpatterns = [
    ... ...
    url(r'^(\d+)/vote/$', views.vote, name='vote'),
]
# 2. 修改detail.html，指定表单提交给vote
        <form action="{% url 'vote' question.id %}" method="post">
# 3. 编写vote函数
# views.py
from django.shortcuts import render, redirect

def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    choice_id = request.POST.get('choice_id')
    # 通过问题取出相应的选项实例
    choice = question.choice_set.get(id=choice_id)
    choice.votes += 1
    choice.save()
	
    # 重定向到结果页，而不是用render。render不会改变浏览器的URL。redirect重定向，将改变url
    return redirect('result', question_id)
```

## 实现投票结果页

```python
# 1. views.py
def result(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'result.html', {'question': question})

# 2. result.html
{% extends 'base.html' %}
{% load static %}
{% block title %}投票结果页{% endblock %}
{% block content %}
    <h1 class="text-center text-warning">
        {{ question.id }}号问题投票结果页
    </h1>
    <table class="table table-striped table-hover table-bordered h4">
        <thead class="h3 bg-primary">
            <tr>
                <td colspan="2">{{ question.question_text }}</td>
            </tr>
        </thead>
        {% for choice in question.choice_set.all %}
            <tr>
                <td>{{ choice.choice_text }}</td>
                <td>{{ choice.votes }}</td>
            </tr>
        {% endfor %}
    </table>
{% endblock %}
```











