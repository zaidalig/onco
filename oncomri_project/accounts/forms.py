from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

ROLE_CHOICES = [
    ('doctor', 'Doctor'),
    ('radiologist', 'Radiologist'),
    ('patient', 'Patient'),
]

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']
        widgets = {
            'password1': forms.PasswordInput(attrs={'id': 'id_password1'}),
            'password2': forms.PasswordInput(attrs={'id': 'id_password2'}),
        }
