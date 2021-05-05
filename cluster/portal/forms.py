from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text="Required")
    username = forms.CharField(label="Username", max_length=50)
    password1 = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput)
    email.widget.attrs['class'] = 'form-control'
    email.widget.attrs['placeholder'] = 'Email'
    username.widget.attrs['class'] = 'form-control'
    username.widget.attrs['placeholder'] = 'Username'
    password1.widget.attrs['class'] = 'form-control'
    password1.widget.attrs['placeholder'] = 'Password'
    password2.widget.attrs['class'] = 'form-control'
    password2.widget.attrs['placeholder'] = 'Confirm Password'
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
