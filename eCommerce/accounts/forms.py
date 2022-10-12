from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    #username = forms.CharField()
    #email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['email',]

    """
    def clean_username(self):
        username = self.cleaned_data.get('username')

        qs = User.objects.filter(username=username)
        if qs.exists():
            raise ValidationError('Username is taken')
        return username
    """
    def clean_email(self):
        email = self.cleaned_data.get('email')

        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email is taken')
        return email

    """
    def clean_password2(self):
        #data = self.cleaned_data
        print (self.cleaned_data)
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        print(password, password2)

        if password is not None and password != password2:
            raise forms.ValidationError('Passwords must match')

        return password2
    """

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password is not None and password != password2:
            raise ValidationError('Passwords must match')
        return cleaned_data

    def save(self,commit=True):
        user = super(RegisterForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        return user

class GuestForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('Email is taken')

        return email


class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput,label='Confirmed Password',)

    class Meta:
        model = User
        fields = ['email']

    def clean_password2(self):
        print (self.cleaned_data)
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2 ')
        print(password,password2)

        if password2 is not None  and password != password2:
            raise ValidationError('Passwords must match')

        return password2

    def save(self,commit=True):

        user = super(UserAdminCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        return user

class UserAdminChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email','password','active','staff','admin']

    def clean_password(self):
        return self.initial["password"]




