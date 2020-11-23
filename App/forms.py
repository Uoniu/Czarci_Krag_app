from django import forms


class LoginForm(forms.Form):
    mail = forms.EmailField(label="E-Mail")
    password = forms.CharField(widget=forms.PasswordInput(), label="Pass")






