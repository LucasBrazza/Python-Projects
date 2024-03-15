from django import forms
from .models import Person
from BloodType.models import BloodType
from City.models import City


class PersonForm(forms.ModelForm):
    rg = forms.RegexField(regex=r'^\d{2}\.\d{3}\.\d{3}-\d$', error_messages = {'invalid': "Field must be entered in the format: 'xx.xxx.xxx-x'."})
    number = forms.IntegerField(required=True)
    
    class Meta:
        model = Person
        fields = (
            'name',
            'rg',
            'bloodTypeId',
            'cityId',
            'street',
            'number'
            )
        
        labels = {
            "bloodTypeId": "Blood Type",
            'cityId': 'City',
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bloodTypeId'].queryset = BloodType.objects.all().order_by('type')
        self.fields['bloodTypeId'].label_from_instance = lambda obj: f"{obj.type} {obj.factor}"
        self.fields['cityId'].queryset = City.objects.all().order_by('name')
        self.fields['cityId'].label_from_instance = lambda obj: f"{obj.name} / {obj.stateId.acronym}"

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.title()