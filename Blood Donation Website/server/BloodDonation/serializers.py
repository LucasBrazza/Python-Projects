from rest_framework import serializers
from .models import BloodDonation

class BloodDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodDonation
        fields = '__all__'