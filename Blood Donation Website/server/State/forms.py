from django import forms
from .models import State

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ('name', 'acronym')
        

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.title()
    
    def clean_acronym(self):
        acronym = self.cleaned_data['acronym']
        return acronym.upper()