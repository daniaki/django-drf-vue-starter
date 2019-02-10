from django.contrib import auth
from django.shortcuts import render, redirect, reverse


def index(request):
    return render(request, template_name='index/index.html')


def robots(request):
    return render(
        request, template_name='index/robots.txt', content_type='text/plain')


def login(request):
    return redirect(reverse('admin:index'))


def logout(request):
    auth.logout(request)
    return redirect("index:index")
