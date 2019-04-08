from django.shortcuts import render_to_response, redirect, HttpResponse, render
from django.http import HttpResponse
from django.utils import timezone
from .models import Appointment
from .forms import AppointmentCreationForm
from .forms import List
from django.views.generic import ListView
from datetime import date
from users.models import CustomUser

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

def view_appointments(request):
    if (request.user.user_type == 0):
        appts=list(Appointment.objects.filter(owner=request.user.EMPLID))
        return render(request, 'view_appointments.html', {'appts':appts})
    else:
        appts=list(Appointment.objects.all())
        return render(request, 'view_appointments.html', {'appts':appts})
        

def delete_appointment(request):
    apt = list(Appointment.objects.all())
    if request.method == "POST":
        Appointment.objects.filter(pk = request.POST.get('to_delete')).delete()
    return render(request, 'delete_appointment.html',{'apt': apt})


def request_appointment(request):
    req = list(Appointment.objects.filter(owner=''))
    if request.method == "POST":
        selected = Appointment.objects.get(pk = request.POST.get('to_request'))
        selected.owner = request.user.EMPLID
        selected.save()
        return redirect('home')
    return render(request, 'request_appointment.html',{'req': req})

    '''apts=Appointment.objects.all()
    all_items=List(request.POST)
    if all_items.is_valid():
        sel_req=all_items.cleaned_data
        selected_req=sel_req['to_request']
        print(selected_req)
        return render(request, 'view_appointments.html', {'apts':apts})
    else:
        print(all_items.errors)
        return render(request, 'view_appointments.html', {'apts':apts})'''
    '''if request.method == "POST":
        apt_form=List(request.POST)
        if apt_form.is_valid():
            apt_form.save()
            all_items=request.POST.get('to_request', True)
        return render_to_response(request, 'view_appointments.html', {'all_items':all_items})
    else:
        all_items=request.POST.get('to_request', True)
        return render_to_response(request, 'view_appointments.html', {'all_items':all_items})'''
