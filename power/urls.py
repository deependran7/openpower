from django.conf.urls import url
from power.views import *

app_name = 'power'

urlpatterns = [
    url(r'^$', Power.as_view(), name='Homepage'),
    url(r'^introduction$', Power.Introduction, name='Introduction'),


    url(r'^digitalcontrol$', DigitalControl.Content, name='DigitalControl'),


 ]
