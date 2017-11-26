from django.conf.urls import url
from power.views import *

app_name = 'power'

urlpatterns = [
    url(r'^$', Power.Homepage, name='Homepage'),
    url(r'^notes$', Power.Notes, name='Notes'),
    url(r'^tutorials$', Power.Tutorials, name='Tutorials'),



 ]
