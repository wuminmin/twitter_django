import traceback

from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
    try:
        print(request)
        print('  ')
        return render_to_response("login.html")
    except:
        print(traceback.format_exc())
        return HttpResponse('500')