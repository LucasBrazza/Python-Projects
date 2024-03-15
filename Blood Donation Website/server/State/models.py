from django.db import models

class State(models.Model):
    name = models.CharField(max_length=50, unique=True)
    acronym = models.CharField(max_length=2, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name +' - '+ self.acronym
    
    def getAcronym(self):
        return self.acronym