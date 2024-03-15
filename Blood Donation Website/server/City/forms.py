from django import forms
from .models import City
from State.models import State

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name', 'stateId')
        labels = { "stateId": "State" }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stateId'].queryset = State.objects.all().order_by('acronym')
        self.fields['stateId'].label_from_instance = lambda obj: obj.acronym
        

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.title()
