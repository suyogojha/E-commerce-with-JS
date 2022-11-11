from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms



class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder': 'Enter UserName'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control my-2', 'placeholder': 'Enter Your Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder': 'Enter Confirm Password'}))
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        