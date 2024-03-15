from django.db import models
from BloodType.models import BloodType
from City.models import City    

class Person(models.Model):
    name = models.CharField(max_length=50)
    rg = models.CharField(max_length=12, unique=True)
    bloodTypeId = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    cityId = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=4)
    complement = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def get_address(self):
        return self.street + ', ' + self.number + ' - ' + self.complement + ' - ' + self.cityId.name + '/' + self.cityId.stateId.acronym

    def __str__(self):
        return f'{self.name} - {self.rg}'