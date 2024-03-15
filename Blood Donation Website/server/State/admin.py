from django.contrib import admin
from .models import State

admin.site.site_header = 'Blood Donation'

admin.site.register(State)