
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

    def PsatPlot(request):
        template = get_template('Computer/psat/plotting.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

    def PsatIntro(request):
        template = get_template('Computer/psat/components.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

    def PsatLoadFlow(request):
        template = get_template('Computer/psat/load flow.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

    def PsatExample(request):
        template = get_template('Computer/psat/example.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

    def PsatGraph(request):
        template = get_template('Computer/psat/graphical network.html')
        context = {

        }
        return HttpResponse(template.render(context, request))



class Matlab(TemplateView):

    def InverseMatrix(request):
        template = get_template('Computer/matlab/inversecomplexmatrix.html')
        context = {

        }
        return HttpResponse(template.render(context, request))


class Simulink(TemplateView):

    def SeriesRC(request):
        template = get_template('Computer/simulink/responseRC.html')
        context = {

        }
        return HttpResponse(template.render(context, request))
