from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader

class Power(TemplateView):
    template_name = 'power/homepage.html'

    def Introduction(request):
        template = loader.get_template('power/Introduction.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

    def Uploadfiles(request):
        template = loader.get_template('power/form.html')
        context = {

        }
        return HttpResponse(template.render(context,request))