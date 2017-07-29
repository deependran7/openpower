from django.conf.urls import url
from blog.views import *

app_name = 'blog'

urlpatterns = [
    url(r'^$', posts_list, name='homepage'),
    url(r'^create/', posts_create, name='create'),
    url(r'^(?P<id>\d+)/',posts_detail, name='detail'),
    url(r'^(?P<id>\d+)/delete/$', posts_delete, name='delete'),

]
