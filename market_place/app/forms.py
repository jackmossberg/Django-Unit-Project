from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'name',
        'class': 'w-full py-4 px-6 rounded-xl',
        }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'password',
        'class': 'w-full py-4 px-6 rounded-xl',
        }))


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'account name',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
     'placeholder': 'email',
     'class': 'w-full py-4 px-6 rounded-xl',
 }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
     'placeholder': 'password',
     'class': 'w-full py-4 px-6 rounded-xl',
 })), 
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Confirm Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user