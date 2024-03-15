from django import forms
from .models import BloodCenter
from City.models import City

class BloodCenterForm(forms.ModelForm):
    number = forms.IntegerField(required=True)
    
    class Meta:
        model = BloodCenter
        fields = ('name', 'street', 'number', 'complement', 'cityId')
        labels = { "cityId": "City" }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cityId'].queryset = City.objects.all().order_by('name')
        self.fields['cityId'].label_from_instance = lambda obj: f"{obj.name} / {obj.stateId.acronym}"
        self.fields['complement'].required = False
        
    def clean_name(self):
        name = self.cleaned_data['name']
        return name.title()
    
    def clean_street(self):
        street = self.cleaned_data['street']
        return street.title()
    
    
