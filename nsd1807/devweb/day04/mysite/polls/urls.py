from django.conf.urls import url
from . import views    # 使用相对导入的方式，在当前包中导入views模块

# 在http://x.x.x.x/polls/后面开始匹配
urlpatterns = [
    # 首页用views.index函数处理，为这个URL起个名字叫index
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>\d+)/result/$', views.result, name='result'),
]
