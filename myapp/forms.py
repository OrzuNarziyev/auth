from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2','is_staff']

        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Foydalanuvchi'}),
            'email':forms.EmailInput(attrs={'placeholder':'email'}),
            'password1':forms.PasswordInput(attrs={'placeholder':'parol'}),
            'password2':forms.PasswordInput(attrs={'placeholder':'confimation password'}),

        }
