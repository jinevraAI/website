from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Subscriber
from .utils import SendSubscriberMail
import os


def home(request):
    return render(request, 'index.html', {})


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email_address', '')
        email_qs = Subscriber.objects.filter(email_address=email)
        if email_qs.exists():
            data = {"status" : "404"}
            return JsonResponse(data)
        else:
            Subscriber.objects.create(email_address=email)
            SendSubscriberMail(email)
    return HttpResponse("/")
