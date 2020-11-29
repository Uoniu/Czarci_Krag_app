
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import App.forms
import App.models


# ==========================================guest
def guest_home(request):
    obj = App.models.Aktualnosci.objects.all()
    return render(request, 'guest/home.html', {"obj": obj})


# ==========================================user
def logout(request):
    context = {}
    return render(request, 'user/logout.html', context)


def user_bookings(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
    return render(request, 'user/user_bookings.html', context)


def user_points(request):
    context = {}
    return render(request, 'user/user_points.html', context)


def user_profile(request):
    context = {}
    return render(request, 'user/user_profile.html', context)


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


def faq(request):
    context = {}
    return render(request, 'shared/faq.html', context)


def login(request):

    if request.method == 'POST':
        form = App.forms.LoginForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['mail']
            password = form.cleaned_data['password']
            obj = App.models.Aktualnosci.objects.all()

            try:
                user = App.models.Uzytkownik.objects.get(email=mail)
                if user.Haslo == password:
                    request.session['userid'] = user.id.__str__()
                    return render(request, 'guest/home.html', {"obj": obj, "user": user})
            except AssertionError as error:
                guest_home(request)
    else:
        form = App.forms.LoginForm()
        return render(request, 'shared/login.html', {"form": form})


# ==========================================manager
def all_boots(request):
    context = {}
    return render(request, 'manager/all_boots.html', context)


def all_reservations(request):
    context = {}
    return render(request, 'manager/all_reservations.html', context)


def notifications(request):
    context = {}
    return render(request, 'manager/notifications.html', context)


# ==========================================admin
def all_users(request):
    context = {}
    return render(request, 'power/all_users.html', context)


def all_programs(request):
    context = {}
    return render(request, 'power/all_programs.html', context)


