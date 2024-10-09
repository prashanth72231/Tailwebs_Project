from django.contrib.auth.forms import AuthenticationForm
from django import forms

class TeacherLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
