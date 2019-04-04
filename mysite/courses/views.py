from django.shortcuts import render, redirect
from .forms import AddClassForms

# Create your views here.
def courses_add(request):
    if request.method == "POST":
        form = AddClassForms(request.POST)
        if form.is_valid():
            a_form = form.save(commit=False)
            a_form.save()
            return redirect('home')
    else:
        form = AddClassForms()
    return render(request, 'courses_add.html', {'form': form})
