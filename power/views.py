from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template, render_to_string

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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            question = request.POST.get('question','')

            recipints = ['deependran.neupane@gmail.com']

            send_mail(name, question, email,recipints)
    else:
        form = ContactForm()

    return render(request,'form.html', {'form':form})






class DigitalControl(TemplateView):
    template_name = 'DigitalControl/DigitalControl.html'


class ComputerSol(TemplateView):
    template_name = 'Computer/homepage.html'



