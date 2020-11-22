
# Create your views here.
from django.shortcuts import render, redirect
from App.models import Test


def index(request):
    obj = Test.objects.all()
    return render(request, 'App/index.html', {"obj": obj})


def login(request):
    return render(request, 'App/login.html', {})

