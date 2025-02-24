from django import forms
from student.models import  *

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude =['username']
        courses = [
        ('Python Fullstack Development', 'Python Fullstack Development'),
        ('Java Fullstack Development', 'Java Fullstack Development'),
        ('MERN Fullstack Development', 'MERN Fullstack Development'),
        ('Fullstack Testing', 'Fullstack Testing')
       ]
        widgets ={
            'course':forms.RadioSelect(choices=courses)
        }


class StudentUserForm(forms.ModelForm):
    class Meta:
        model =User
        fields =['first_name','last_name','email','username','password']
        help_texts = {'username': ' '}
        
