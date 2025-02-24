from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EmployeeProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    pno = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    class Meta:
        db_table ='employee_profile'

    def __str__(self):
        return self.username.username
