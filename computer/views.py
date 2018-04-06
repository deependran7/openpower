
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect, request
from django.template.loader import get_template
# Create your views here.

class Computer(TemplateView):

    def Index(request):
        template = get_template('Computer/homepage.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

    def Matlab(request):
        template = get_template('Computer/matlab.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

    def Simulink(request):
        template = get_template('Computer/simulink.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

    def Psat(request):
        template = get_template('Computer/psat.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

    def PsatInstall(request):
        template = get_template('Computer/psat/install.html')
        context = {

        }
        return HttpResponse(template.render(context, request))
