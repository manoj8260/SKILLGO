from django.shortcuts import render,redirect
from manager.forms import *
from django.views.generic import View
from django.http import HttpResponse
from django.core.mail import  send_mail
from django.contrib.auth import authenticate,login,logout
# Create your views here.


class HrHome(View):
    def get(self,request):
        return render(request,'hr/home.html')
    
class HrLogin(View):
    def get(self,request):
          return render(request,'hr/login.html')
    def post(self,request):
         un = request.POST.get('username')
         pw = request.POST.get('password')
         AHO  = authenticate(request,username  = un ,password = pw)
         if AHO and AHO.is_active and AHO.is_staff :
              PO  = EmployeeProfile.objects.get(username = AHO)
              if PO.role == 'HR':
                   login(request,AHO)
                   request.session['hruser'] = un 
                   return redirect('hr_home')
              return HttpResponse('you are not validate user')
         return HttpResponse('credentials do not match')

def hr_logout(request):
     logout(request)
     return render(request,'hr/home.html')    
         