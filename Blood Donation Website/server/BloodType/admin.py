from django.contrib import admin
from .models import BloodType

admin.site.site_header = 'Blood Donation'

admin.site.register(BloodType)