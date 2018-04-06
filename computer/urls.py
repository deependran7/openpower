from django.conf.urls import url
from computer.views import *

app_name = 'computer'

urlpatterns = [
    url(r'^$', Computer.Index, name='Homepage'),
    url(r'^matlab$', Computer.Matlab, name='Matlab'),
    url(r'^simulink$', Computer.Simulink, name='Simulink'),
    url(r'^psat$', Computer.Psat, name='Psat'),

    url(r'^psatinstall$', Computer.PsatInstall, name='PsatInstall'),




]
