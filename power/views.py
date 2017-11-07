from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template.loader import get_template

from django.core.mail import send_mail
from power.forms import ContactForm


class Power(TemplateView):
    template_name = 'Homepage.html'

    def Introduction(request):
        template = get_template('Introduction.html')
        context = {

        }
        return HttpResponse(template.render(context, request))




class DigitalControl(TemplateView):

    def Content(request):
        template = get_template('DigitalControl/DigitalControl1.html')
        context = {


        }
        return HttpResponse(template.render(context, request))




class ComputerSol(TemplateView):
    template_name = 'Computer/homepage.html'



