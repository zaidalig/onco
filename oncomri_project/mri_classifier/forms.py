from django import forms
from .models import MRIImage

class MRIImageForm(forms.ModelForm):
    class Meta:
        model = MRIImage
        fields = ['image']
