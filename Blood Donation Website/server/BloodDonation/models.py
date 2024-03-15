from django.db import models
from Person.models import Person
from BloodCenter.models import BloodCenter
from Person.models import Person
from BloodType.models import BloodType

class BloodDonation(models.Model):
    personId = models.ForeignKey(Person, on_delete=models.CASCADE)
    bloodCenterId = models.ForeignKey(BloodCenter, on_delete=models.CASCADE)
    date = models.DateField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)   
    
    def get_donnor(self):
        return Person.objects.get(pk=self.personId).name
    
    def get_blood_type(self):
        return BloodType.objects.get(pk=self.bloodTypeId).get_complete_blood_type()