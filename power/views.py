from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from .models import UploadFile
import tempfile
from subprocess import Popen, PIPE
import os

class Power(TemplateView):
    template_name = 'Introduction.html'

    def Introduction(request):
        template = get_template('Introduction.html')
        context = {

        }
        return HttpResponse(template.render(context, request))



    #def DigitalControl(request):
    #    template = get_template('DigitalControl/DigitalControl.html')
     #   context = {

      #  }

        return HttpResponse(template.render(context, request))

def Uploadfiles(request):
    template = get_template('form.html')
    context = {

    }

    return  HttpResponse(template.render(context, request))

class HomePageView(TemplateView):
    template_name = 'DigitalControl/DigitalControl.html'

