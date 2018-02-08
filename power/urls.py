from django.conf.urls import url
from power.views import *

app_name = 'power'

urlpatterns = [
    url(r'^$', Power.Homepage, name='Homepage'),
    url(r'^notes$', Power.Notes, name='Notes'),
    url(r'^tutorials$', Power.Tutorials, name='Tutorials'),

    url(r'^Utillisation$', Power.Utillisation, name='Utillisation'),
    url(r'^Material$', Power.Material, name='Material'),



 ]
