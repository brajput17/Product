from django import forms
from . import models
from dataclasses import field, fields

class UsersForm(forms.ModelForm):
    name=forms.CharField(max_length=20,label="Name")
    email=forms.EmailField(label="Email ")
    username=forms.CharField(max_length=20,label="User Name ")
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = models.Users
        fields = {'name','email','username','password'}
