from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your full name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Your email'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'Your message'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'gmail.com' not in email:
            raise forms.ValidationError('Email has to be gmail.com')
        return email


