from django import forms
from student.models import  *

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude =['username']
        widgets ={
            'course':forms.RadioSelect
        }


class StudentUserForm(forms.ModelForm):
    class Meta:
        model =User
        fields =['first_name','last_name','email','username','password']
        help_texts = {'username': ' '}
        
