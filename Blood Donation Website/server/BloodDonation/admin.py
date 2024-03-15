from django.contrib import admin
from .models import BloodDonation

admin.site.site_header = 'Blood Donation'

admin.site.register(BloodDonation)