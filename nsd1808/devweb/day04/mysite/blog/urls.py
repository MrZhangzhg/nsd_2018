from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='blog_index'),
    url(r'^(?P<article_id>\d+)/$', views.show_article, name='show_article'),
]
