from django.db import models
from django.contrib.auth.models import User
# Create your models here
subjects =[
    ('Python','Python'),
    ('Java','Java'),
    ('JavaScript','JavaScript'),
    ('SQL','SQL'),
    ('Django','Django'),
    ('React','React'),
    ('SpringBoot','SpringBoot'),
]
rattings =[
    ('*','*'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
]


class Ratings(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name='rating')
    subject  = models.CharField(max_length=250,choices=subjects)
    communication = models.CharField(max_length=50,choices=rattings)
    technical = models.CharField(max_length=50,choices=rattings)
    programming = models.CharField(max_length=50,choices=rattings)
    conducted_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='conducted_by')
    conducted_on = models.DateTimeField(auto_now=True,auto_now_add=False)
    remarks = models.CharField(max_length=250,default='')


    class Meta:
        db_table = 'student_rating'

    def __str__(self):
        return f"{self.student.username} ----> {self.subject}"
