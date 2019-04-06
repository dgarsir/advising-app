from django.shortcuts import render, redirect
from django.views import generic

from advising.models import Advising

def Home(request):

    authenticated = request.user.is_authenticated
    
    if authenticated:

        user_type = request.user.user_type

        if (user_type == 0):

            #gets advising form status by checking Advising model for EMPLID match
            adv_form = Advising.objects.filter(author = request.user.EMPLID)
            adv_status = 0

            if len(adv_form) != 0:
                adv_form = list(adv_form)[0]
                adv_status = adv_form.status

            adv_message = ''

            if adv_status == 0:
                adv_message = "Unadvised"
            if adv_status == 1:
                adv_message = "Advisement pending."
            if adv_status == 2:
                adv_message = "Advisement pending final approval."
            if adv_status == 3:
                adv_message = "Advised.  Thank you for using QuickReg."
            return render(request, 'home.html', {
                'adv_message' : adv_message,
                'adv_status' : adv_status,
                'adv_form' : adv_form
            })
        
        else:   

            if (user_type == 1):
                to_be_advised = Advising.objects.filter(total_credits__gte=45).filter(status = 1)
            else:
                to_be_advised = Advising.objects.filter(status = 2)
            
            if request.method=="POST":
                request.session['selected_id'] = request.POST.get('selected_form')
                #for some reason redirect works and render doesn't?
                #idk don't change it
                return redirect('view_advising_faculty')

            return render(request, 'home.html', {
                'to_be_advised' : to_be_advised
            })

    return render(request, 'home.html')