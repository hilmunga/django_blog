# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.conf.urls.static import static

# Create your views here.

def post_list(request):
    posts= Post.objects.filter(published_date=timezone.now()).order_by("published_date")
    return render(request, 'abilityhemu_blog/post_list.html', {'posts':posts} )
def menu_show(request):
    post=Post.objects.all()
    return render(request, 'abilityhemu_blog/menu.html', {'post':post})
def lipalater(request):
    return render(request, 'abilityhemu_blog/lipa later.html')
def post_detail(request,pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request,'abilityhemu_blog/post_detail.html', {'post':post})






