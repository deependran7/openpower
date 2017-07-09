from django.conf.urls import url
from computer.views import *

app_name = 'computer'

urlpatterns = [
    url(r'^$', index, name='Homepage'),
    url(r'^introduction$', Matlab, name='Introduction'),
    url(r'^matlab$', Simulink, name='MatlabBasics'),
    url(r'^simulink$', Raspberry, name= 'Simulink'),


]
