from django import forms
import App.models


class Datetimeinput(forms.DateInput):
    input_type = 'datetime-local'


class LoginForm(forms.Form):
    mail = forms.EmailField(label="E-Mail", required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label="Pass", required=True)


class Rezerwacjaform(forms.Form):
    data_rozpoczeczia = forms.DateTimeField(widget=Datetimeinput,input_formats=['%Y-%m-%d %H:%M:%S'])
    data_zakonczenia = forms.DateTimeField(widget=Datetimeinput, input_formats=['%Y-%m-%d %H:%M:%S'])
    uwagi = forms.CharField(max_length=50)
    usluga = forms.ModelChoiceField(queryset=App.models.Uslugi.objects.all())






