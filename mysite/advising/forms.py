from django import forms
from .models import Advising

class SubmitAdvisingForm(forms.ModelForm):
    class Meta:
        model = Advising
        fields = (
            'semester',
            'major',
            'QPA',
            'GPA',
            'currently_enrolled',
            'completed_courses'
        )
