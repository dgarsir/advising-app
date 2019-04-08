#import webapp2 
from django.contrib import admin
#import django.template.loader as dj
from .models import Appointment

admin.site.register(Appointment)
