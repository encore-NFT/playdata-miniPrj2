from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import User


class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

class PasswordResetRequestForm(forms.Form):
    email = forms.CharField(label=("Email"), max_length=254)



