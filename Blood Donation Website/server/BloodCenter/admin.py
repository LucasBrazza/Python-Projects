from django.contrib import admin
from .models import BloodCenter

admin.site.site_header = 'Blood Donation'

admin.site.register(BloodCenter)