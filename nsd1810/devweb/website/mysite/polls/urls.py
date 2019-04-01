from django.conf.urls import url
from . import views

urlpatterns = [
    # url(URL的正则, 对应的函数, url的名称)
    url(r'^$', views.index, name='index'),
]
