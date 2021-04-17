from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.contrib.auth import authenticate
from .models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(help_text="A valid email id is required")

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'is_startup_founder', 'password1', 'password2')

class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login Credentials")
