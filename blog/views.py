from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
from django.contrib import messages
from .models import *
# Create your views here.


def posts_list(request):
    queryset_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list":queryset,
    }
    return render(request, 'blog/post_list.html', context)









def posts_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Thank you for your issue.")

        return HttpResponseRedirect(reverse('blog:homepage'))
    else:
        messages.error(request, "Sorry, not valid data.")
    context = {
        "form":form,
    }
    return render(request, "blog/post_form.html",context)

def posts_update(request):
    return HttpResponse('<h1>my posts</h1>')

def posts_delete(request):
    return HttpResponse('<h1>my posts</h1>')