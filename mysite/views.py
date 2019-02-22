from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,"index.html")


def information(request):
    return render(request, "information.html")


def buy(request):
    return render(request, "buy.html")


def scenery(request):
    return render(request, "scenery.html")


def about(request):
    return render(request, "about.html")


def speedtest(request):
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']

    return HttpResponse( ip )

