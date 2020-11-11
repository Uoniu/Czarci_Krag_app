
# Create your views here.
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'App/index.html', context=None)