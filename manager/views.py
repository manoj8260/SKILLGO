from django.shortcuts import render,redirect
from manager.forms import *
from django.views.generic import View
import random
import string
from django.http import HttpResponse
from django.core.mail import  send_mail
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class ManagerHome(View):
    def get(self,request):
        return render(request,'manager/home.html')
    
class AddEmployee(View):
    def get(self,request):
        EEUFO = EmployeeUserForm()
        EEPFO = EmployeeProfileForm()
        context ={
            'EEUFO':EEUFO,
            'EEPFO':EEPFO,
        }
        return render(request,'manager/add_employee.html',context)  
     
    def post(self,request):
        EUFDO=EmployeeUserForm(request.POST)
        EPFDO =EmployeeProfileForm(request.POST)
        if EUFDO.is_valid() and EPFDO.is_valid():
            email= EUFDO.cleaned_data.get('email')
            un = f'{EUFDO.cleaned_data.get('first_name')}{EPFDO.cleaned_data.get('pno')[-4:]}'
            pw = ''.join(random.choices(string.ascii_letters,k =5) + random.choices(string.digits,k=2) +random.choices(string.punctuation,k=1) )
            MEUFDO = EUFDO.save(commit=False)
            MEUFDO.username = un
            MEUFDO.set_password(pw)
            MEUFDO.is_staff =True
            MEPFDO = EPFDO.save(commit=False)
            MEPFDO.username = MEUFDO
            MEUFDO.save()
            MEPFDO.save()
            message = f'hello {EUFDO.cleaned_data.get('first_name')}{EPFDO.cleaned_data.get('last_name')} \n \t your username is : {un} and your password is : {pw} \n \t welcome to our application  '
            send_mail (
                  'register as employee',
                   message,
                  'kumarmanoj8260910@gmail.com',
                  [email],
                  fail_silently = False    
                 )
            return  HttpResponse('done')
        return HttpResponse('invalid data')


class ManagerLogin(View):
    def get(self,request):
        return render(request,'manager/login.html')
    def post(self,request):
        un = request.POST.get('username')
        pw = request.POST.get('password')
        AMO= authenticate(request,username = un ,password = pw)
        if AMO :
            if  AMO.is_active and AMO.is_staff and AMO.is_superuser:
               login(request,AMO)
               request.session['adminuser'] = un
               return  redirect('manager_home')
            return HttpResponse('you are not superuser')
        return HttpResponse('credentials do not match')
        


def manager_logout(request):
    logout(request)
    return render(request,'manager/login.html')
