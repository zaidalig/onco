from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
        ('radiologist','Radiologist'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')
