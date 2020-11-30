from django import forms
import App.models


class Datetimeinput(forms.DateInput):
    input_type = 'datetime-local'


class LoginForm(forms.Form):
    mail = forms.EmailField(label="E-Mail", required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label="Hasło", required=True)


class Rezerwacjaform(forms.Form):
    data_rozpoczeczia = forms.DateTimeField(widget=Datetimeinput,input_formats=['%Y-%m-%d %H:%M:%S'])
    data_zakonczenia = forms.DateTimeField(widget=Datetimeinput, input_formats=['%Y-%m-%d %H:%M:%S'])
    uwagi = forms.CharField(max_length=50)
    usluga = forms.ModelChoiceField(queryset=App.models.Uslugi.objects.all())


class Uzytkownikform(forms.Form):
    TypUzytkownika = forms.ChoiceField(choices=[('Użytkownik','Użytkownik'),('Administrator','Administrator')], required=False)
    Imie = forms.CharField(max_length=50)
    Nazwisko = forms.CharField(max_length=80)
    email = forms.CharField(max_length=100)
    NrTelefonu = forms.CharField(max_length=15)


class FaqAskForm(forms.Form):
    Tytul=forms.CharField(max_length=50)
    Tresc=forms.CharField(max_length=200)


class MailForm(forms.Form):
    To = forms.EmailField(max_length=200,)
    Cc = forms.EmailField(max_length=200, required=False)
    Subject = forms.CharField()
    Msg = forms.CharField(widget=forms.Textarea())


class AddToProgram(forms.Form):
    Uzytkownik = forms.ModelChoiceField(queryset=App.models.Uzytkownik.objects.filter(TypUzytkownika="Użytkownik"))






