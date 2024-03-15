from django.db import models
from State.models import State

class City(models.Model):
    name = models.CharField(max_length=50)
    stateId = models.ForeignKey(State, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def getNameAndState(self):
        state = State.getAcronym(pk=self.stateId)
        return self.name + ' / ' + state
    
    def getCityState(self):
        return State.getAcronym(self.stateId)
