
# Create your views here.
from django.shortcuts import render, redirect
from App.models import Test
from django.contrib.auth import authenticate, login


# ========================================================================= guest
def index(request):
    obj = Test.objects.all()
    return render(request, 'guest_module/home.html', {"obj": obj})


def login(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
    return render(request, 'guest_module/login.html', {})


def prices(request):
    return render(request, 'guest_module/prices.html', {})


def gallery(request):
    return render(request, 'guest_module/gallery.html', {})


def about(request):
    return render(request, 'guest_module/about.html', {})


def contact(request):
    return render(request, 'guest_module/contact.html', {})


# ========================================================================= admin
def admin_home(request):
    obj = Test.objects.all()
    return render(request, 'admin_module/home.html', {"obj": obj})


# ======================================================================== manager
def manager_home(request):
    obj = Test.objects.all()
    return render(request, 'manager_module/home.html', {"obj": obj})


# ======================================================================== user
def user_home(request):
    obj = Test.objects.all()
    return render(request, 'user_module/home.html', {"obj": obj})

def user_data(request):
    obj = Test.objects.all()
    return render(request, 'user_module/data.html', {"obj": obj})

def user_reserve(request):
    obj = Test.objects.all()
    return render(request, 'user_module/reserve.html', {"obj": obj})

def user_program(request):
    obj = Test.objects.all()
    return render(request, 'user_module/program.html', {"obj": obj})


# ======================================================================== worker
def worker_home(request):
    obj = Test.objects.all()
    return render(request, 'worker_module/home.html', {"obj": obj})


# ======================================================================== shared
def logout(request):
    return render(request, 'shared/logout.html', {})

