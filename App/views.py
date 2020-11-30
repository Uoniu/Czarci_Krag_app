
# Create your views here.

from django.shortcuts import render, redirect
import App.forms
import App.models


# =================================================================================================== guest
def guest_home(request):
    context = {'obj': App.models.Aktualnosci.objects.all()}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
    return render(request, 'guest/home.html', context)


# ======================================================================================================== user
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
            if request.POST.get('bookid'):
                tmp = App.models.Rezerwacja.objects.get(id=request.POST.get('bookid'))
                tmp.delete()
                return redirect(user_bookings)
            form = App.forms.Rezerwacjaform(request.POST)
            if form.is_valid():
                tmp_rezerwacja = App.models.Rezerwacja()
                tmp_rezerwacja.Uwagi = form.cleaned_data['uwagi']
                tmp_rezerwacja.DataRozpoczecia = form.cleaned_data['data_rozpoczeczia']
                tmp_rezerwacja.DataZakonczenia = form.cleaned_data['data_zakonczenia']
                tmp_rezerwacja.IdUslugi = form.cleaned_data['usluga']
                tmp_rezerwacja.IdUzytkownika = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
                tmp_rezerwacja.save()
                return redirect(user_bookings)
        else:
            form = App.forms.Rezerwacjaform()
            context['form'] = form
            context['bookinglist'] = App.models.Rezerwacja.objects.filter(IdUzytkownika_id=request.session.get('userid'))
            return render(request, 'user/user_bookings.html', context)
    else:
        return redirect(guest_home)


def user_points(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        context['program'] = App.models.ProgramLojalnosciowy.objects.filter(IdUzytkownika_id=request.session.get('userid'))
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


# =================================================================================================== shared
def prices(request):
    context = {'ceny': App.models.Aktualnosci.objects.get(Naglowek="Cennik")}
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
    context = {'fq': App.models.FAQ.objects.all()}

    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        context['form'] = App.forms.FaqAskForm()
        if request.POST.get('zmien'):
            tmp_faq = App.models.FAQ.objects.get(id=request.POST.get('zmien'))
            tmp_faq.Odpowiedz = request.POST.get('odpowiedz')
            tmp_faq.save()
            return redirect(faq)
        if request.method == 'POST':
            form = App.forms.FaqAskForm(request.POST)
            if form.is_valid():
                tmp_faq = App.models.FAQ()
                tmp_faq.Tresc = form.cleaned_data['Tresc']
                tmp_faq.Tytul = form.cleaned_data['Tytul']
                tmp_faq.Odpowiedz = "Jeszcze nie ma odpowiedzi"
                tmp_faq.save()
                return redirect(faq)

    return render(request, 'shared/faq.html', context)


def login(request):
    context = {}
    if request.method == 'POST':
        form = App.forms.LoginForm(request.POST)

        if form.is_valid():
            mail = form.cleaned_data['mail']
            password = form.cleaned_data['password']
            try:
                user = App.models.Uzytkownik.objects.get(email=mail)
            except:
                return redirect(login)

            if user.Haslo == password:
                context['user'] = user
                request.session['userid'] = context['user'].id.__str__()
                context['obj'] = App.models.Aktualnosci.objects.all()
                return render(request, 'guest/home.html', context)
            else:
                return redirect(login)

    context['form'] = App.forms.LoginForm()
    return render(request, 'shared/login.html', context)


# ==================================================================================================== manager
def all_boots(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        context['boots'] = App.models.Buty.objects.all()
        return render(request, 'manager/all_boots.html', context)
    else:
        return redirect(guest_home)


def all_reservations(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        context['bookinglist'] = App.models.Rezerwacja.objects.all()
        if request.method == 'POST':
            if request.POST.get('bookid'):
                tmp = App.models.Rezerwacja.objects.get(id=request.POST.get('bookid'))
                tmp.delete()
                return redirect(all_reservations)
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


# ================================================================================================== admin
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
    context = {}
    if request.session.get('idnum'):
        user = App.models.Uzytkownik.objects.get(id=request.session.get('idnum'))
        context['activeuser'] = user
    elif request.session.get('userid'):
        user = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        context['activeuser'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
    else:
        redirect(guest_home)
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
    if request.method == "POST":
        form = App.forms.Uzytkownikform(request.POST)
        if request.POST.get('delete'):
            if user.id == request.session.get('userid'):
                user.delete()
                del request.session['userid']
                return redirect(guest_home)
            user.delete()
            return redirect(guest_home)
        if request.POST.get('edit'):
            if form.is_valid():
                tmp_user = App.models.Uzytkownik(id=user.id)
                tmp_user.Imie = form.cleaned_data['Imie']
                tmp_user.Nazwisko = form.cleaned_data['Nazwisko']
                tmp_user.email = form.cleaned_data['email']
                if form.cleaned_data['TypUzytkownika']:
                    tmp_user.TypUzytkownika = form.cleaned_data['TypUzytkownika']
                else:
                    tmp_user.TypUzytkownika = "Użytkownik"
                tmp_user.NrTelefonu = form.cleaned_data['NrTelefonu']
                tmp_user.Haslo = user.Haslo
                tmp_user.save()
                return redirect(guest_home)
    form = App.forms.Uzytkownikform()
    form.fields['Imie'].initial = user.Imie
    form.fields['Nazwisko'].initial = user.Nazwisko
    form.fields['NrTelefonu'].initial = user.NrTelefonu
    form.fields['email'].initial = user.email
    form.fields['TypUzytkownika'].initial = user.TypUzytkownika
    context['form'] = form
    return render (request, 'power/all_users_tmp.html', context)


def all_programs(request):
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        context['programs'] = App.models.ProgramLojalnosciowy.objects.all().order_by('id')
        if request.method == "POST":
            form = App.forms.AddToProgram(request.POST)
            context['form'] = App.forms.AddToProgram()
            if form.is_valid():
                tmp = App.models.ProgramLojalnosciowy()
                tmp.IdUzytkownika = form.cleaned_data['Uzytkownik']
                tmp.Punkty = 0
                tmp.Nagroda = "brak"
                tmp.save()
                return render(request, 'power/all_programs.html', context)
        else:
            context['form'] = App.forms.AddToProgram()
        if request.POST.get('dodaj'):
            if request.POST.get('punkty'):
                tmp = App.models.ProgramLojalnosciowy.objects.get(id=request.POST.get('dodaj'))
                tmp.Punkty += int(request.POST.get('punkty'))
                tmp.save()
                return redirect(all_programs)
        if request.POST.get('zmiana'):
            if request.POST.get('nagroda'):
                tmp = App.models.ProgramLojalnosciowy.objects.get(id=request.POST.get('zmiana'))
                tmp.Nagroda = request.POST.get('nagroda')
                tmp.save()
                return redirect(all_programs)
        return render(request, 'power/all_programs.html', context)
    else:
        return redirect(guest_home)


def add_user (request):
    context = {}
    if request.method == "POST":
        form = App.forms.Uzytkownikform(request.POST)
        if form.is_valid():
            tmp = App.models.Uzytkownik()
            tmp.Imie = form.cleaned_data['Imie']
            tmp.Nazwisko = form.cleaned_data['Nazwisko']
            tmp.email = form.cleaned_data['email']
            tmp.NrTelefonu = form.cleaned_data['NrTelefonu']
            tmp.TypUzytkownika = "Użytkownik"
            if request.POST.get('pass') == request.POST.get('repass'):
                tmp.Haslo = request.POST.get('pass')
            else:
                context['badpass'] = "1"
                context['form'] = App.forms.Uzytkownikform()
                return render(request, 'shared/add_user.html', context)
            tmp.save()
            request.session['userid'] = tmp.id
            return redirect(guest_home)
        print("nie wchodzi")
        redirect(login)
    context['form'] = App.forms.Uzytkownikform()
    return render(request, 'shared/add_user.html', context)



