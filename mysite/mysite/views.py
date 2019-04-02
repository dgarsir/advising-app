from django.shortcuts import render
from django.views import generic

from advising.models import Advising

def Home(request):
    
    if request.user.is_authenticated:

        #gets advising form status by checking Advising model for EMPLID match
        adv_form = Advising.objects.filter(author = request.user.EMPLID)
        adv_status = 0

        if len(adv_form) != 0:
            print("adv_check != 0")
            adv_form = list(adv_form)[0]
            adv_status = adv_form.status

        return render(request, 'home.html', {
            'adv_status' : adv_status,
            'adv_form' : adv_form
        })
    
    return render(request, 'home.html')