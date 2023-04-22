from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Customer, User

class CustomerRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=200)

    class Meta:
        model = Customer
        fields = ('name', 'email', 'password1', 'password2')

class CustomerLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')