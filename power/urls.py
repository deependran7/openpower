from django.conf.urls import url
from power.views import *

app_name = 'power'

urlpatterns = [
    url(r'^$', Power.as_view(), name='homepage'),
    url(r'^introduction$', Power.Overview, name='Overview'),


    url(r'^digitalcontrol$', DigitalControl.Content, name='DigitalControl'),


    url(r'^uploadfiles$',Uploadfiles, name='Upload'),

]
