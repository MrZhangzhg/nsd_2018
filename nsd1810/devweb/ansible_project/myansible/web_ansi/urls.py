from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^addhosts/$', views.addhosts, name='addhosts'),
    url(r'^addmodules/$', views.addmodules, name='addmodules'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^delargs/(?P<args_id>\d+)/$', views.delargs, name='delargs'),
]
