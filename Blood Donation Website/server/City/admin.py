from django.contrib import admin
from .models import City

admin.site.site_header = 'Blood Donation'

admin.site.register(City)