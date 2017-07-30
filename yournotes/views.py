from django.http import Http404
from django.shortcuts import render
from .forms import UploadFileForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages
from .models import NotesUpload
# Create your views here.


def note_save(request):
    if request.user.is_staff or request.user.is_superuser or request.user.is_authenticated:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('yournotes'))
        else:
            messages.error(request,"Sorry,not valid data.")
        context = {
            "form":form,
        }
        return render(request, "notes/Notesupload.html", context)
    else:
        raise Http404



def note_view(request):
    notesets = NotesUpload.objects.all()
    context = {
        "notes": notesets,
    }
    return render(request,"notes/NoteView.html",context)







