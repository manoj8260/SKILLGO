from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import os
# Create your models here.

class StudentProfile(models.Model):
    courses = [
        ('Python Fullstack Development', 'Python Fullstack Development'),
        ('Java Fullstack Development', 'Java Fullstack Development'),
        ('MERN Fullstack Development', 'MERN Fullstack Development'),
        ('Fullstack Testing', 'Fullstack Testing')
       ]
    def rename_resume(self,filename):
        exe = filename.split('.')[-1]
        new_filename = f'{self.username.first_name}_{self.username.last_name}.{exe}'

        return os.path.join('students_resumes',new_filename)
    
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    pno = models.CharField(max_length=50)
    add = models.TextField()
    course = models.CharField(max_length=50, default='Python Fullstack Development',choices=courses)
    profile_pic = models.ImageField(upload_to='students_profiles/',null=True,blank=True)
    resume = models.FileField(upload_to=rename_resume,
                              validators=[FileExtensionValidator(['pdf','doc'])]
                              )
    class Meta:
        db_table ='student_profile'

    def __str__(self):
        return self.username.username
    
    