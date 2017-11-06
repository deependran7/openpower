from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template, render_to_string
# Create your views here.

def index(request):
    template = get_template('Computer/homepage.html')
    context = {

    }
    return HttpResponse(template.render(context, request))



def Matlab(request):
    pass


def Simulink(request):
    pass

def Raspberry(reqest):
    pass

def Psat(request):
    template = get_template('Computer/psat.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
