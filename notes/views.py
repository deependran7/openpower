from django.http import HttpResponse
from django.shortcuts import render
from .models import UploadFile

from .forms import UploadFileForm
# Create your views here.
from django.template.loader import get_template


def UploadNotes(request):
    form = UploadFileForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    template = get_template('yournotes/upload file.html')
    context = {
                "form":form,
    }
    return HttpResponse(template.render(context, request))


def Notes(request):

    queryset = UploadFile.objects.all()

    template = get_template('yournotes/notesandsol.html')
    context = {
            "noteslist":queryset
    }
    return HttpResponse(template.render(context, request))