# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404,redirect
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
from.forms import Postform

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
def post_new(request):
    if request.method=='POST':
     form =Postform(request.POST)
     if form.is_valid():
         post=form.save(commit=False)
         post.author=request.user
         post.published_date=timezone.now()
         post.save()
         return redirect('post_detail',pk=post.pk)
    else:
     form =Postform()
    return render(request, 'abilityhemu_blog/post_edit.html',{'form':form})
def post_edit(request, pk):
   post = get_object_or_404(Post, pk=pk)
   if request.method == "POST":
    form = Postform(request.POST, instance=post)
    if form.is_valid():
     post = form.save(commit=False)
     post.author = request.user
     post.published_date = timezone.now()
     post.save()
    return redirect('post_detail', pk=post.pk)
   else:
    form = Postform(instance=post)
   return render(request, 'abilityhemu_blog/post_edit.html', {'form': form})






