
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # make sure models.py has CustomUser class

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']

