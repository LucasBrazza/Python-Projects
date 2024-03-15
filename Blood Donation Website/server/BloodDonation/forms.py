from django import forms
from .models import BloodDonation
from Person.models import Person
from BloodCenter.models import BloodCenter

class BloodDonationForm(forms.ModelForm):
    
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = BloodDonation
        fields = ('personId', 'bloodCenterId', 'date')
        labels = {
            'personId': 'Donor',
            'bloodCenterId': 'Blood Center',
        }    
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['personId'].queryset = Person.objects.all().order_by('name')
        self.fields['bloodCenterId'].queryset = BloodCenter.objects.all().order_by('name')  
        
    
    
    
        