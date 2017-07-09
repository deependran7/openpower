from django.conf.urls import url
from power.views import *

app_name = 'power'

urlpatterns = [
    url(r'^$', Power.as_view(), name='homepage'),
    url(r'^introduction00$', Power.Introduction, name='Introduction'),
    url(r'^digitalcontrol$', DigitalControl.as_view(), name='DigitalControl'),
    #url(r'^computersol$', ComputerSol.as_view(), name= 'computerhome'),
    url(r'^uploadfiles$',Uploadfiles, name='Upload'),

]
