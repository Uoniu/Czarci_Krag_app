from django import forms
from django.contrib.auth import authenticate

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

