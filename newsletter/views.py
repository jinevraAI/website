from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .utils import SendSubscriberMail
import os


def home(request):
    return render(request, 'index.html', {})


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email_address', '')
        mc = SendSubscriberMail(email)
        if mc:
            data = {"status": "200"}
        else:
            data = {"status" : "404"}
        return JsonResponse(data)

    return HttpResponse("/")
