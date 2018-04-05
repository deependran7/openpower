from django.conf.urls import url
from .views import *

app_name = 'notes'

urlpatterns = [
    url(r'^$', Notes, name='Notes'),

    url(r'^upload$', UploadNotes, name='UploadNotes'),




 ]
