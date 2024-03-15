from django.db import models
from City.models import City

class BloodCenter(models.Model):
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=4)
    complement = models.CharField(max_length=50)
    cityId = models.ForeignKey(City, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name + ' - ' + self.cityId.name

    def get_address(self):
        return self.street + ', ' + self.number + ' - ' + self.complement + ' - ' + self.cityId.name + '/' + self.cityId.stateId.acronym
    
    def getCity(self):
        return City.__str__(pk=self.cityId)
    
    def getCityInfo(self):
        return City.getNameAndState(pk=self.cityId)
    
    def getNameCityState(self):
        return self.name + ' - ' + City.getNameAndState(pk=self.cityId)

