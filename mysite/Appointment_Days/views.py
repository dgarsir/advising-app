from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Appointment
from django.template import loader
from django.http import HttpResponse
from .forms import AppointmentCreationForm


def add_appointment(request):
    if request.method == "POST":
        form = AppointmentCreationForm(request.POST)
        if form.is_valid():
            a_form = form.save(commit=False)
            a_form.save()
            return redirect('home')
    else:
        form = AppointmentCreationForm()
    return render(request, 'add_appointment.html', {'form': form})