from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # Qodo: Test this class
    class Meta:
        model = User
        fields = ['username', 'email']


# Qodo: Test this class
class ProfileUpdateForm(forms.ModelForm):

    # Qodo: Test this class
    class Meta:
        model = Profile
        fields = ['image']