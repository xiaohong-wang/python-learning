from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your full name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Your email'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'Your message'}))

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    def clean_username(self):
        username = self.cleaned_data.get('username')

        qs = User.objects.filter(username=username)
        if qs.exists():
            raise ValidationError('Username is taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email is taken')
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('Passwords must match')

        return data

