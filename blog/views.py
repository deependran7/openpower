from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
from django.contrib import messages
from .models import *
from django.db.models import Q
from blogcomment.models import Comment
from blogcomment.forms import CommentForm
#from django.contrib.auth.decorators import login_required
# Create your views here.


def posts_list(request):
    queryset_list = Post.objects.all().order_by("-timestamp")
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query)

        ).distinct()

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
        "object_list": queryset,
    }

    return render(request, 'blog/post_list.html', context)


def posts_create(request):
    if request.user.is_staff or request.user.is_superuser or request.user.is_authenticated:

        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Thank you for your issue.")

            return HttpResponseRedirect(reverse('blog:homepage'))
        else:
            messages.error(request, "Sorry, not valid data.")
            context = {
                "form": form,
            }
        return render(request, "blog/post_form.html", context)
    else:
        raise Http404


def posts_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)

    initial_data = {
        "content_type":instance.get_content_type,
        "object_id" : instance.id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        new_comment, created = Comment.objects.get_or_create(
            user = request.user,
            content_type = content_type,
            object_id = obj_id,
            content = content_data
        )
        if created:
            print("ok done")

        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

    comments = Comment.objects.filter_by_instance(instance)

    context = {
        "title": instance.title,
        "instance": instance,
        "comments":comments,
        "comment_form":form,
    }
    return render(request, "blog/post_detail.html", context)


def posts_update(request):
    return HttpResponse('<h1>my posts</h1>')


def posts_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect('blog:homepage')
