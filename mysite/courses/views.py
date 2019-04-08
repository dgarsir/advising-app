from django.shortcuts import render, redirect
from .forms import AddClassForms
from .models import Courses

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

def view_courses(request):
    print(request.POST)
    queryset=Courses.objects.all()
    context ={
        "object_list": queryset,
        "title": "list"
    }
    '''if request.method == "POST":
        for obj in queryset:
            print(obj.courses_name)
            print(obj.teacher)
        return redirect('home')'''
    return render(request, 'view_courses.html',context)


def del_course(request):
    course = list(Courses.objects.all())
    if request.method == "POST":
        Courses.objects.filter(pk = request.POST.get('to-delete')).delete()
    return render(request,'del_course.html', {'course': course})

