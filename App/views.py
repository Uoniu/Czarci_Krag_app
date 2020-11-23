
# Create your views here.
from django.shortcuts import render, redirect
from App.models import Aktualnosci
from App.models import Uzytkownik
import App.forms


# ==========================================guest
def guest_home(request):
    obj = Aktualnosci.objects.all()
    return render(request, 'guest/home.html', {"obj": obj})


# ==========================================user
def logout(request):
    context = {}
    return render(request, 'user/logout.html', context)

def user_bookings(request):
    context = {}
    return render(request, 'user/user_bookings.html', context)

def user_points(request):
    context = {}
    return render(request, 'user/user_points.html', context)


# ==========================================shared
def prices(request):
    context = {}
    return render(request, 'shared/prices.html', context)


def gallery(request):
    context = {}
    return render(request, 'shared/gallery.html', context)


def about(request):
    context = {}
    return render(request, 'shared/about.html', context)


def contact(request):
    context = {}
    return render(request, 'shared/contact.html', context)


def login(request):

    if request.method == 'POST':
        form = App.forms.LoginForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['mail']
            password = form.cleaned_data['password']
            user = Uzytkownik.objects.get(email=mail)
            obj = Aktualnosci.objects.all()

            try:
                user = Uzytkownik.objects.get(email=mail)
                if user.Haslo == password:
                    return render(request, 'guest/home.html', {"obj": obj, "user": user})
            except AssertionError as error:
                guest_home(request)
    else:
        form = App.forms.LoginForm()
        return render(request, 'shared/login.html', {"form": form})
