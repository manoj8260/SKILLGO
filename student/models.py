from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.

class StudentProfile(models.Model):
    

    

    username = models.ForeignKey(User, on_delete=models.CASCADE)
    pno = models.CharField(max_length=50)
    add = models.TextField()
    course = models.CharField(max_length=50, default='Python Fullstack Development')
    profile_pic = models.ImageField(upload_to='students_profiles/',null=True,blank=True)
    resume = models.FileField(upload_to='students_resumes/',validators=[FileExtensionValidator(['pdf','word'])])

    class Meta:
        db_table ='student_profile'

    def __str__(self):
        return self.username.username
    
    