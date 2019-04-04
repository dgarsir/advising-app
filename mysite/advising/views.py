from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone

from .forms import SubmitAdvisingForm
from .models import Advising
from users.models import CustomUser

# Create your views here.

def submit_advising(request):
    if request.method == "POST":
        form = SubmitAdvisingForm(request.POST)
        if form.is_valid():
            a_form = form.save(commit=False)
            a_form.author = request.user.EMPLID
            a_form.date_submitted = timezone.now()
            a_form.status = 1
            a_form.save()
            return redirect('home')
    else:
        form = SubmitAdvisingForm()
    return render(request, 'submit_advising.html', {'form': form})

def view_advising_faculty(request):

    a_form = list(Advising.objects.filter(pk = request.session['selected_id']))[0]
    f_name = CustomUser.objects.get(EMPLID = a_form.author).first_name
    l_name = CustomUser.objects.get(EMPLID = a_form.author).last_name

    return render(request, 'view_advising_faculty.html', {
    'f_name' : f_name,
    'l_name' : l_name,
    'semester' : a_form.semester,
    'major' : a_form.major,
    'QPA' : a_form.QPA,
    'GPA' : a_form.QPA, 
    'currently_enrolled' : a_form.currently_enrolled,
    'completed_courses' : a_form.completed_courses,
    'total_credits' : a_form.total_credits,
    'date_submitted' : a_form.date_submitted
    })


def view_advising(request):

    a_form = list(Advising.objects.filter(author = request.user.EMPLID))[0]
    if request.method == "POST":
        Advising.objects.filter(author = request.user.EMPLID).delete()
        return redirect('home')
    return render(request, 'view_advising.html', {
        'semester' : a_form.semester,
        'major' : a_form.major,
        'QPA' : a_form.QPA,
        'GPA' : a_form.QPA, 
        'currently_enrolled' : a_form.currently_enrolled,
        'completed_courses' : a_form.completed_courses,
        'total_credits' : a_form.total_credits,
        'date_submitted' : a_form.date_submitted
    })
    