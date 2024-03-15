from rest_framework import serializers
from .models import BloodCenter

class BloodCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodCenter
        fields = '__all__'