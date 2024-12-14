
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Musician
from django import forms


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'email', 'address', 'birth_date', 'instrument', 'phone_number'] # Remove password from fields/form
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))
    
