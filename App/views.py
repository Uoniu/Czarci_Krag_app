
# Create your views here.

from django.shortcuts import render, redirect
import App.forms
import App.models


# ==========================================guest
def guest_home(request):
    context = {'obj': App.models.Aktualnosci.objects.all()}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
    return render(request, 'guest/home.html', context)


# ==========================================user
def logout(request):
    if request.method == 'GET':
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout' and 'userid' in request.session:
                request.session.flush()
                return redirect(guest_home)


def user_bookings(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        if request.method == 'POST':
            form = App.forms.Rezerwacjaform(request.POST)
            if form.is_valid():
                tmp_rezerwacja = App.models.Rezerwacja()
                tmp_rezerwacja.Uwagi = form.cleaned_data['uwagi']
                tmp_rezerwacja.DataRozpoczecia = form.cleaned_data['data_rozpoczeczia']
                tmp_rezerwacja.DataZakonczenia = form.cleaned_data['data_zakonczenia']
                tmp_rezerwacja.IdUslugi = form.cleaned_data['usluga']
                tmp_rezerwacja.IdUzytkownika = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
                tmp_rezerwacja.save()
                return redirect(guest_home)
        else:
            form = App.forms.Rezerwacjaform()
            context['form'] = form
            return render(request, 'user/user_bookings.html', context)
    else:
        return redirect(guest_home)


def user_points(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        return render(request, 'user/user_points.html', context)
    else:
        return redirect(guest_home)


def user_profile(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        return render(request, 'user/user_profile.html', context)
    else:
        return redirect(guest_home)


# ==========================================shared
def prices(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
    return render(request, 'shared/prices.html', context)


def gallery(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
    return render(request, 'shared/gallery.html', context)


def about(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
    return render(request, 'shared/about.html', context)


def contact(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
    return render(request, 'shared/contact.html', context)


def faq(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
    return render(request, 'shared/faq.html', context)


def login(request):
    context = {}
    if request.method == 'POST':
        form = App.forms.LoginForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['mail']
            password = form.cleaned_data['password']

            try:
                context['user'] = App.models.Uzytkownik.objects.get(email=mail)
                if context['user'].Haslo == password:
                    request.session['userid'] = context['user'].id.__str__()
                    context['obj'] = App.models.Aktualnosci.objects.all()
                    return render(request, 'guest/home.html', context)
            except AssertionError as error:
                guest_home(request)
    else:
        context['form'] = App.forms.LoginForm()
        return render(request, 'shared/login.html', context)


# ==========================================manager
def all_boots(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        return render(request, 'manager/all_boots.html', context)
    else:
        return redirect(guest_home)


def all_reservations(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        return render(request, 'manager/all_reservations.html', context)
    else:
        return redirect(guest_home)


def notifications(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        return render(request, 'manager/notifications.html', context)
    else:
        return redirect(guest_home)


# ==========================================admin
def all_users(request):
    context = {}
    if request.session.get('userid'):
        if request.method == "POST":
            request.session['idnum'] = request.POST.get("idnum", "")
            return redirect(user_details)
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        context['userlist'] = App.models.Uzytkownik.objects.all()
        return render(request, 'power/all_users.html', context)
    else:
        return redirect(guest_home)


def user_details(request):
    context = {'activeuser': App.models.Uzytkownik.objects.get(id=request.session.pop('idnum'))}
    render (request,'power/all_users_tmp.html',context)


def all_programs(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        return render(request, 'power/all_programs.html', context)
    else:
        return redirect(guest_home)



