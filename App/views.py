# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from Czarci_Krag.settings import EMAIL_HOST_USER
import App.forms
import App.models

# =================================================================================================== guest
def guest_home(request): #logika obsługująca panel główny
    context = {'obj': App.models.Aktualnosci.objects.all()}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
    return render(request, 'guest/home.html', context)


# ======================================================================================================== user
def logout(request): #logika panelu wylogowania użytkownika, przy spełnienu warunków requesta parametr użytkownika usuwany jest z sesji
    if request.method == 'GET':
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout' and 'userid' in request.session:
                request.session.flush()
                return redirect(guest_home)


def user_bookings(request): #logika obsługująca rezerowanie usługi przez użytkownika
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        if request.method == 'POST':
            if request.POST.get('bookid'):
                tmp = App.models.Rezerwacja.objects.get(id=request.POST.get('bookid'))

                #bookid jest zmienną otrzymaną z ządania html, jej wartość odpowiada wartości id rezerwacji wybranej przez użytkownika

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

                # Jeżeli form otrzymany ze strony za pomocą żądania post, przejdzie przez walidację zapewnioną przez django, dane z formularza wpisywane są
                # do zmiennej tymczasowej, która jest obiektem modelu rezerwacja, w celu zapisania danej do bazy danych przez metodę obiektu klasy modelowej

                return redirect(user_bookings)

        else:

            form = App.forms.Rezerwacjaform()
            context['form'] = form
            context['bookinglist'] = App.models.Rezerwacja.objects.filter(IdUzytkownika_id=request.session.get('userid'))

            # jeżeli żądanie nie jest typu post, oznacza to, że nie został wypełniony żaden formularz, dlatego do zawartości dodawanej do renderowanej strony
            # dodawawany jest pusty formularz dodawania rezerwacji i lista rezerwacji danego użytkownika w celu ich wyświetlenia

            return render(request, 'user/user_bookings.html', context)
    else:
        return redirect(guest_home)


def user_points(request):  #logika strony punktacji programu lojanościowego użytkownika, wyświetla punkty aktualnie zalogowanego użytkownika.

    context = {}
    if request.session.get('userid'):

        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        context['program'] = App.models.ProgramLojalnosciowy.objects.filter(IdUzytkownika_id=request.session.get('userid'))
        return render(request, 'user/user_points.html', context)

    else:

        return redirect(guest_home)


def user_profile(request):  #do zawartosci strony wczytywane są z bazy danych tylko dane aktualnie zalogowanego w sesji użytkownika
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        return render(request, 'user/user_profile.html', context)
    else:
        return redirect(guest_home)


# =================================================================================================== shared
def prices(request):   #strona wyświetla informacje, nie jest zapewniona w niej zaawansowana logika, poza rozpoznawaniem użytkownika w celu pokazania poprawnego masterpage
    context = {'ceny': App.models.Aktualnosci.objects.get(Naglowek="Cennik")}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
    return render(request, 'shared/prices.html', context)


def gallery(request):  #strona wyświetla informacje, nie jest zapewniona w niej zaawansowana logika, poza rozpoznawaniem użytkownika w celu pokazania poprawnego masterpage
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
    return render(request, 'shared/gallery.html', context)


def about(request):#strona wyświetla informacje, nie jest zapewniona w niej zaawansowana logika, poza rozpoznawaniem użytkownika w celu pokazania poprawnego masterpage
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
    return render(request, 'shared/about.html', context)


def contact(request):#strona wyświetla informacje, nie jest zapewniona w niej zaawansowana logika, poza rozpoznawaniem użytkownika w celu pokazania poprawnego masterpage
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
    return render(request, 'shared/contact.html', context)


def faq(request): #logika obsługi modułu odpowiedzialnego za faq

    context = {'fq': App.models.FAQ.objects.all()}

    if request.session.get('userid'):

        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        context['form'] = App.forms.FaqAskForm()


        if request.POST.get('zmien'):

            tmp_faq = App.models.FAQ.objects.get(id=request.POST.get('zmien'))
            tmp_faq.Odpowiedz = request.POST.get('odpowiedz')
            tmp_faq.save()

            # Jeżeli w wysłanym żądaniu wysłana zostanie zmienna zmien przypisana do przycisku w html,
            # oznacza to przyciśnięcie przez użytkownika przycisku odpowiedzialnego za zmianę odpowiedzi

            return redirect(faq)

        if request.method == 'POST':

            form = App.forms.FaqAskForm(request.POST)

            if form.is_valid():

                tmp_faq = App.models.FAQ()
                tmp_faq.Tresc = form.cleaned_data['Tresc']
                tmp_faq.Tytul = form.cleaned_data['Tytul']
                tmp_faq.Odpowiedz = "Jeszcze nie ma odpowiedzi"
                tmp_faq.save()

                # Przepisywane z formularza do utworzenia nowego obiektu typu FAQ są dane, do zmiennej tymczasowej, w celu wykorzystania metody save

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

                #jeżeli nie zostanie oczytany mail z formularza, albo nie zostanie znaleziony odpowiadający mu użytkownik
                # albo użytkownik o danym mailu nie istnieje, albo formularz został wypełniony źle

            except:

                context['form'] = App.forms.LoginForm()
                context['badpass'] = True

                #przy błędnym wypełnieniu formularza logowania, zostaje załadowany nowy formularz,
                # oraz zmienna badpass w zawartości zostanie ustawiona na true, w celu obsługi powiadamiania użytkownika o błędnych danych

                return render(request, 'shared/login.html', context)

            if user.Haslo == password:

                context['user'] = user
                request.session['userid'] = context['user'].id.__str__()
                context['obj'] = App.models.Aktualnosci.objects.all()

                # jeżeli wszystkie testy przejdą pomyślnie do sesji zostaje dodana zmienna odpowiadająca za id aktualnie zalogowanego użytkownika

                return render(request, 'guest/home.html', context)

            else:

                context['form'] = App.forms.LoginForm()
                context['badpass'] = True
                return render(request, 'shared/login.html', context)

    context['form'] = App.forms.LoginForm()
    return render(request, 'shared/login.html', context)


# ==================================================================================================== manager
def all_boots(request):#strona wyświetla informacje, nie jest zapewniona w niej zaawansowana logika, poza rozpoznawaniem użytkownika w celu pokazania poprawnego masterpage
    context = {}
    if request.session.get('userid'):
        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        context['boots'] = App.models.Buty.objects.all()
        return render(request, 'manager/all_boots.html', context)
    else:
        return redirect(guest_home)


def all_reservations(request): #strona posługująca się tą logiką, wyświetla dla administratora wszystkie rezerwacje oraz daje możliwość ich usuwania
    context = {}

    if request.session.get('userid'):

        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        context['bookinglist'] = App.models.Rezerwacja.objects.all()

        # jeżeli nie było żądania typu post, strona wyświetla tylko wszystkie rezerwacje,
        # jeżeli zostało wysłane żądanie typu post, oznacza to kliknięcie przez administratora
        # przycisku odpowiadającego za usunięcie jednej z rezerwacji

        if request.method == 'POST':

            if request.POST.get('bookid'):

                tmp = App.models.Rezerwacja.objects.get(id=request.POST.get('bookid'))

                # bookid jest nazwą klikniętego guzika, którego wartością jest id przyciśniętej rezerwacji

                tmp.delete()
                return redirect(all_reservations)

        return render(request, 'manager/all_reservations.html', context)

    else:

        return redirect(guest_home)


def notifications(request): #logika modułu wysyłania powiadomień do użytkownika, korzysta z SMTP

    context = {}

    if request.session.get('userid'):

        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        context['form'] = App.forms.MailForm()

        #jeżeli nie zostało wysłane żądanie typu post, na stronie renderowany jest pusty formularz

        if request.method == 'POST':

            form = App.forms.MailForm(request.POST)

            if form.is_valid():

                to = form.cleaned_data['To']
                subject = form.cleaned_data['Subject']
                msg = form.cleaned_data['Msg']

                # po sprawdzeniu poprawności formularza, wywoływana jest funkcja send_mail zaimportowana z pythona,
                # mail wysyłany jest z podpiętego adresu e-mail należącego do czarciego kręgu, odpowiada za niego
                # zmienna EMAIL_HOST_USER

                send_mail(
                    subject,
                    msg,
                    EMAIL_HOST_USER,
                    [to],
                )

                context['mail'] = "True"
        context['form'] = App.forms.MailForm()

        return render(request, 'manager/notifications.html', context)
    else:
        return redirect(guest_home)


# ================================================================================================== admin

def all_users(request):

    context = {}

    if request.session.get('userid'):

        if request.method == "POST":

            if request.POST.get('idnum'):

                request.session['idnum'] = request.POST.get("idnum", "")
                return redirect(user_details)

            if request.POST.get('search'):

                context['userlist'] = App.models.Uzytkownik.objects.filter(Nazwisko__contains=request.POST.get('search_text'))
                context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
                return render(request, 'power/all_users.html', context)

        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        context['userlist'] = App.models.Uzytkownik.objects.all()

        return render(request, 'power/all_users.html', context)

    else:

        return redirect(guest_home)


def user_details(request): #logika strony szczegółów użytkownika

    context = {}

    if request.session.get('idnum'):

        user = App.models.Uzytkownik.objects.get(id=request.session.get('idnum'))
        context['activeuser'] = user

    elif request.session.get('userid'):

        user = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))
        context['activeuser'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))

    else:

        redirect(guest_home)

    # Ze względu na możliwość przekierowania na stronę użytkownika oraz administratora,
    # sprawdzane jest na początku czy w sesji jest zapisana zmienna userid oznaczająca
    # że przeniesienie nastąpiło z panelu administratora, jeżeli nie jest ona przesłana
    # w sesji, przeniesienie nastąpiło z panelu użytkownika

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

            # Jeżeli w żądaniu wysłana została zmienna delete, oznacza to wybranie przycisku chęci usunięcia konta
            # w takim przypadku jeżeli zostanie usunięte konto użytkownika, który jest aktualnie zalogowany,
            # z sesji zostanie usunięta zmienna identyfikująca tego użytkownika, jeżeli administrator
            # usuwa konto innego użytkownika, zostanie przekierowany na ekran główny

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

            # Jeżeli w żądaniu wysłana została zmienna edit, oznacza to chęć edycji danych użytkownika,
            # w takim przypadku pobierane są dane z formularza i jeżeli jest on poprawny, nowe dane
            # zapisywane są w bazie danych

    form = App.forms.Uzytkownikform()
    form.fields['Imie'].initial = user.Imie
    form.fields['Nazwisko'].initial = user.Nazwisko
    form.fields['NrTelefonu'].initial = user.NrTelefonu
    form.fields['email'].initial = user.email
    form.fields['TypUzytkownika'].initial = user.TypUzytkownika
    context['form'] = form

    # Jeżeli żadne żądanie nie zostało wysłane do logiki aplikacji, folmularz edycji,
    # wypełniany jest aktualnymi danymi użytkownika, którego dane mogą być edytowane

    return render (request, 'power/all_users_tmp.html', context)


def all_programs(request): #logika obsługi progarmu lojalnościowego przez administratora

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

            # Jeżeli w żądaniu wysłany został formularz dodania nowego programu lojalnościowego
            # jest on dodawany z automatycznymi wartościami 0 punktów i braku nagrody, w przeciwnym wypadku
            # generowany jest pusty formularz

        else:

            context['form'] = App.forms.AddToProgram()

        if request.POST.get('dodaj'):

            if request.POST.get('punkty'):

                tmp = App.models.ProgramLojalnosciowy.objects.get(id=request.POST.get('dodaj'))
                tmp.Punkty += int(request.POST.get('punkty'))
                tmp.save()
                return redirect(all_programs)

            # wysłanie formularza za pomocą przycisku dodaj, uruchamia logikę
            # edytującą aktualną liczbę punktów konkretnego programu lojalnościowego
            # id programu przeysłane jest jako wartość samego przycisku, a wartość o jaką
            # należy poprawić liczbę, w polu tekstowym


        if request.POST.get('zmiana'):

            if request.POST.get('nagroda'):

                tmp = App.models.ProgramLojalnosciowy.objects.get(id=request.POST.get('zmiana'))
                tmp.Nagroda = request.POST.get('nagroda')
                tmp.save()
                return redirect(all_programs)

                # tak samo nagroda, edytowana jest kiedy zostanie wysłany w żądaniu przycisk zmiana
                # którego wartość odpowiada id programu, a wybrana z listy nagroda zapisana jest w bazie
                # jako nowa wartość

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

            # jeżeli  zostanie spełniona walidacja formularzu przesłanego wcześniej w żądaniu post
            # dane wpisane w formularzu dodawania nowego użytkownika przypisane są do zmiennej tymczasowej
            # następuje po tym sprawdzenie poprawności haseł zapisanych z pól hasła oraz powtórzenia hasła

            if request.POST.get('pass') == request.POST.get('repass'):

                tmp.Haslo = request.POST.get('pass')

            else:

                context['badpass'] = "1"
                context['form'] = App.forms.Uzytkownikform()
                return render(request, 'shared/add_user.html', context)

            # jeżeli hasło i powtórzone hasło się zgadzają,to do zmiennej tymczasowej typu modelu użytkownika
            # dodawane jest to hasło, oraz obiekt zapisywany jest do bazy danych. jeżeli nie to renderowana
            # jest strona ze zmienną w zawartości, mówiącą o powtórzeniu złego hasła

            tmp.save()
            request.session['userid'] = tmp.id
            return redirect(guest_home)

        redirect(login)

    context['form'] = App.forms.Uzytkownikform()
    return render(request, 'shared/add_user.html', context)

def add_news(request):

    context = {}

    if request.session.get('userid'):

        context['user'] = App.models.Uzytkownik.objects.get(id=request.session.get('userid'))

    if request.method == "POST":

        form = App.forms.AddNews(request.POST)

        if form.is_valid():

            tmp = App.models.Aktualnosci()
            tmp.Tresc = form.cleaned_data['Content']
            tmp.Naglowek = form.cleaned_data['Title']
            tmp.Istotnosc = form.cleaned_data['Istotnosc']
            tmp.save()
            return redirect(guest_home)

        # wczytywany jest formularz dodawania aktualności, jeżeli został on wypełniony
        # poprawnie, zapisywany jest w bazie danych nowy obiekt modelu aktualności z tymi danymi
        # w przeciwnym razie formularz jest czyszczony i renderowany ponownie

    context['form'] = App.forms.AddNews()
    return render(request, 'manager/add_news.html', context)