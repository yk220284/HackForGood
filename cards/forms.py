from django import forms
from .models import Player, Card


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name']
        labels = {'name': 'name'}
