from django.conf.urls import url
from blog.views import *

app_name = 'blog'

urlpatterns = [
    url(r'^$', posts_list, name='homepage'),
    url(r'^create/', posts_create, name='create'),
    url(r'^update/', posts_update, name='update'),
    url(r'^delete/', posts_delete, name='delete'),
]
