from django import forms
from hr.models import *

class SchedulingsForm(forms.ModelForm):
    class Meta:
        model =MockScheduling
        fields='__all__'
        help_texts = {'student': 'only accept  CSV file*'}