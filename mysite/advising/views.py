from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from .forms import SubmitAdvisingForm

# Create your views here.

def submit_advising(request):
    if request.method == "POST":
        form = SubmitAdvisingForm(request.POST)
        if form.is_valid():
            a_form = form.save(commit=False)
            a_form.author = request.user.EMPLID
            a_form.date_submitted = timezone.now()
            a_form.save()
            return redirect('home')
    else:
        form = SubmitAdvisingForm()
    return render(request, 'submit_advising.html', {'form': form})
