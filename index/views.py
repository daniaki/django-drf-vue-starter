from django.shortcuts import render


def index(request):
    return render(request, template_name='index/index.html')


def robots(request):
    return render(
        request, template_name='index/robots.txt', content_type='text/plain')
