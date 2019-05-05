from django.conf.urls import url
from . import views   # 在当前目录(包)中导入views模块

# polls应用的正则表达式，从http://x.x.x.x/polls/后面开始匹配
urlpatterns = [
    # 首页用veiws.index函数响应，为这个URL起名为index
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
]
