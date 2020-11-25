from django import forms


class LoginForm(forms.Form):
    mail = forms.EmailField(label="E-Mail")
    password = forms.CharField(widget=forms.PasswordInput(), label="Pass")

class testform(forms.Form):
    col = forms.CharField(label="cool")


class testformdel(forms.Form):
    colid = forms.IntegerField(label = "id")

class testformalt(forms.Form):
    colidd = forms.IntegerField(label = "id")
    coll = forms.CharField(label="cool")

class simplelogin (forms.Form):
    one = forms.CharField(label="id")
    two = forms.CharField(label="big D")






