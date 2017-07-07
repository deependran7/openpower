from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template, render_to_string
import tempfile
from subprocess import Popen, PIPE
import os
from django.core.mail import send_mail, BadHeaderError
from power.forms import ContactForm

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


def Uploadfiles(request):
    template = get_template('form.html')
    context = {

    }
    return HttpResponse(template.render(context, request))



class DigitalControl(TemplateView):
    template_name = 'DigitalControl/DigitalControl.html'


class ComputerSol(TemplateView):
    template_name = 'Computer/homepage.html'



