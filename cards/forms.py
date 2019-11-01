from django import forms

choices = (('red', 'red'), ('blue', 'blue'))


class ChangeColourForm(forms.Form):
    colour = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
