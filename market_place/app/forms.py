from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'password','confirmpassword')

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Desired account name please',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
     'placeholder': 'Personal email please',
     'class': 'w-full py-4 px-6 rounded-xl',
 }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
     'placeholder': 'Desired password please',
     'class': 'w-full py-4 px-6 rounded-xl',
 }))
    confirmpassword = forms.CharField(widget=forms.TextInput(attrs={
     'placeholder': 'Please confirm password',
     'class': 'w-full py-4 px-6 rounded-xl',
 }))