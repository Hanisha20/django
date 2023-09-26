from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs= {'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs= {'class': 'form-control'}))
    password1 = forms.CharField(label='password' ,widget=forms.PasswordInput(attrs= {'class': 'form-control'}))
    password2 = forms.CharField(label='rep-password' ,widget=forms.PasswordInput(attrs= {'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('The email address is already existing')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('The username is already existing')
        return username
    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')
        if p1 and p2 and p1 != p2:
            raise ValidationError('The password is not match')
            
class UserLoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs= {'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs= {'class': 'form-control'}))

class UserRegistrationForm2(forms.Form):
    username = forms.CharField()
    nickName = forms.CharField()
    lastName = forms.CharField()
    birthDate = forms.DateField()
    codeMeli = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)