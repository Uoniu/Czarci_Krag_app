from django import forms
import App.models


class Datetimeinput(forms.DateInput): #klasa rozszerzająca widget DateInput, służąca do zmiany podstawowego typu wprowadzaniej danej na datetime-local
    input_type = 'datetime-local'


class LoginForm(forms.Form): #formularz służący do wysłania danych do uwierzytelnienia użytkownika
    mail = forms.EmailField(label="E-Mail", required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label="Hasło", required=True)


class Rezerwacjaform(forms.Form): #formularz utworzenia nowej rezerwacji, usługa wybierana jest spośród listy dostępnych w ModelChoiceField, a referencja do klucza obcego użytkownika brana z aktualnie zalogowanego użytkownika
    data_rozpoczeczia = forms.DateTimeField(widget=Datetimeinput,input_formats=['%Y-%m-%d %H:%M:%S'])
    data_zakonczenia = forms.DateTimeField(widget=Datetimeinput, input_formats=['%Y-%m-%d %H:%M:%S'])
    uwagi = forms.CharField(max_length=50)
    usluga = forms.ModelChoiceField(queryset=App.models.Uslugi.objects.all())


class Uzytkownikform(forms.Form): #formularz wykorzystywany do utworzenia oraz edycji obiektu użytkownika systemu
    TypUzytkownika = forms.ChoiceField(choices=[('Użytkownik','Użytkownik'), ('Kierownik','Kierownik'), ('Administrator','Administrator')], required=False)
    Imie = forms.CharField(max_length=50)
    Nazwisko = forms.CharField(max_length=80)
    email = forms.CharField(max_length=100)
    NrTelefonu = forms.CharField(max_length=15)


class FaqAskForm(forms.Form): #formularz utworzenia pytania do FAQ
    Tytul=forms.CharField(max_length=50)
    Tresc=forms.CharField(max_length=200)


class MailForm(forms.Form): #formularz potrzebnych danych do wysłania powiadomienia przez SMTP
    To = forms.ModelChoiceField(queryset=App.models.Uzytkownik.objects.filter(TypUzytkownika="Użytkownik"))
    Subject = forms.CharField()
    Msg = forms.CharField(widget=forms.Textarea())


class AddToProgram(forms.Form): #formularz wyboru użytkownika, służy do dodawania do programu lojalnościowego
    Uzytkownik = forms.ModelChoiceField(queryset=App.models.Uzytkownik.objects.filter(TypUzytkownika="Użytkownik"))


class AddNews(forms.Form): #formularz dodawania nowego obiektu aktualności
    Title = forms.CharField(max_length=50)
    Content = forms.CharField(widget=forms.Textarea(), max_length=200)
    Istotnosc = forms.ChoiceField(choices=[('1','mało istotne'),('2','istotne'),('3','bardzo istotne')])






