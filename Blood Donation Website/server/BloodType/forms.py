from django import forms
from .models import BloodType

class BloodTypeForm(forms.ModelForm):
    
    type = forms.ChoiceField(choices=BloodType.BLOOD_TYPE_OPTIONS, initial='' )
    factor = forms.ChoiceField(choices=BloodType.BLOOD_FACTOR_OPTIONS, initial='' )
    
    class Meta:
        model = BloodType
        fields = ('type', 'factor')
        

    def clean_type(self):
        type = self.cleaned_data['type']
        return type.upper()