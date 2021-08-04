from django import forms
from .models import Melody

class MelodyForm(forms.ModelForm):
    class Meta:
        model=Melody
        fields = '__all__'