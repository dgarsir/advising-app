from django.db import models
from django.utils import timezone

class Appointment(models.Model):
	date=models.DateField(default=timezone.localdate)
	start_time=models.TimeField(default=timezone.now)
	end_time=models.TimeField(default=timezone.now)
	owner=models.CharField(default='', max_length=100)
