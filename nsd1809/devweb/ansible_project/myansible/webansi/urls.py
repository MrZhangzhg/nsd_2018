from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addhosts/$', views.addhosts, name='addhosts'),
    url(r'^addmodules/$', views.addmodules, name='addmodules'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^del_args/(?P<args_id>\d+)/$', views.del_args, name='del_args'),
]
