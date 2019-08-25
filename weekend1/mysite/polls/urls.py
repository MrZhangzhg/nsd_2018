from django.conf.urls import url
from . import views   # 相对导入，从当前目录中导入views模块

urlpatterns = [
    # 当访问应用首页时，用views.index函数处理
    # 该url(http://x.x.x.x/polls/)命名为index
    url(r'^$', views.index, name='index'),
    # 通过正则\d+匹配数字，再将这个数字作为vies.detail的参数
    url(r'^(\d+)/$', views.detail,name='detail'),
    url(r'^(\d+)/result/$', views.result, name='result'),
]
