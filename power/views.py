from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template.loader import get_template

from django.core.mail import send_mail
from power.forms import ContactForm


class Power(TemplateView):

    def Homepage(request):
        template = get_template('Power/homepage.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

    def Notes(request):
        template = get_template('Power/notesandsol.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

    def Tutorials(request):
        template = get_template('Power/tutorials.html')
        context = {

        }
        return HttpResponse(template.render(context, request))





