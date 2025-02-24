from django import forms
from hr.models import Ratings

class  RattingForm(forms.ModelForm):
    class Meta:
        model = Ratings
        exclude =['conducted_by']
        # fields = '__all__'