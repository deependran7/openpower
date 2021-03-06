from django.conf.urls import url
from computer.views import *

app_name = 'computer'

urlpatterns = [
    url(r'^$', Computer.Index, name='Homepage'),
    url(r'^matlab$', Computer.Matlab, name='Matlab'),
    url(r'^simulink$', Computer.Simulink, name='Simulink'),
    url(r'^psat$', Computer.Psat, name='Psat'),

    url(r'^psatinstall$', Computer.PsatInstall, name='PsatInstall'),
    url(r'^psatplot$', Computer.PsatPlot, name='PsatPlot'),
    url(r'^psatintro$', Computer.PsatIntro, name='PsatIntro'),
    url(r'^psatloadflow$', Computer.PsatLoadFlow, name='PsatLoadFlow'),
    url(r'^psatexample$', Computer.PsatExample, name='PsatExample'),
    url(r'^psatgraph$', Computer.PsatGraph, name='PsatGraph'),



    url(r'^matinverse$', Matlab.InverseMatrix, name='MatInverse'),



    url(r'^simrccircuit$', Simulink.SeriesRC, name='SimRC'),

]
