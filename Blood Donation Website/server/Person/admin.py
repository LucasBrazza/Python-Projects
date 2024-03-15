from django.contrib import admin
from .models import Person

admin.site.site_header = 'Blood Donation'

admin.site.register(Person)