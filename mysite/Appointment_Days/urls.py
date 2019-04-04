from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
	path('add_appointments/', views.add_appointment, name='add_appointments')
]