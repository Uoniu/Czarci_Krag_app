
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from App.models import Aktualnosci
from App.models import Uzytkownik
from App.models import Test
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

# ===================================== db test ===================================
def test(request):

    record = Test.objects.all()
    if request.method == 'POST':
        formatka = App.forms.testform(request.POST)
        formatkadel = App.forms.testformdel(request.POST)
        formatkaalt = App.forms.testformalt(request.POST)
        formatkalogin = App.forms.simplelogin(request.POST)
        if formatka.is_valid():
            test_obj = Test()
            dana = formatka.cleaned_data['col']
            test_obj.col = dana
            test_obj.save()
            return redirect('test')
        if formatkadel.is_valid():
            test_obj = Test.objects.get(id=formatkadel.cleaned_data['colid'])
            test_obj.delete()
            return redirect('test')
        if formatkaalt.is_valid():
            test_obj = Test.objects.get(id=formatkaalt.cleaned_data['colidd'])
            test_obj.col = formatkaalt.cleaned_data['coll']
            test_obj.save()
            return redirect('test')
        if formatkalogin.is_valid():
            formatka = App.forms.testform()
            formatkadel = App.forms.testformdel()
            formatkaalt = App.forms.testformalt()
            formatkalogin = App.forms.simplelogin()
            user = "skema byku"
            return render(request, 'DBTest/Test.html', {"record": record, "form": formatka, "formdel": formatkadel, "formalt": formatkaalt, "formalog": formatkalogin, "user": user})
    else:
        formatka = App.forms.testform()
        formatkadel = App.forms.testformdel()
        formatkaalt = App.forms.testformalt()
        formatkalogin = App.forms.simplelogin()
        return render(request, 'DBTest/Test.html', {"record": record, "form": formatka, "formdel": formatkadel, "formalt": formatkaalt, "formalog": formatkalogin})
