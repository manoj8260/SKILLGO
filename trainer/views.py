from django.shortcuts import render,redirect
from manager.forms import *
from django.views.generic import View
from django.http import HttpResponse
from django.core.mail import  send_mail
from django.contrib.auth import authenticate,login,logout
from trainer.forms import   * 
# Create your views here.

class StartMock(View):
    def get(self,request):
        ERFO = RattingForm()
        context = {'ERFO':ERFO}
        return render(request,'trainer/mock_ratting.html',context)
    def post(self,request):
        RFDO = RattingForm(request.POST)
        if RFDO.is_valid():
            trainer_user = request.session.get('traineruser')
            TO = User.objects.get(username = trainer_user)
            MRFDO = RFDO.save(commit=False)
            MRFDO.conducted_by = TO
            MRFDO.save()
            return redirect('trainer_home')
        return HttpResponse('invalid data')



def trainer_login_required(func):
    def inner(request,*args,**kwargs):
        un = request.session.get('traineruser')
        if un :
            func(request,*args,**kwargs)
        return render(request,'trainer/login.html')  
    return inner 

class TrainerHome(View):
    def get(self,request):
        return render(request,'trainer/home.html')


class TrainerLogin(View):
    def get(self,request):
        return render(request,'trainer/login.html')
    def post(self,request):
        un = request.POST.get('username')
        pw = request.POST.get('password')
        ATO = authenticate(request, username =  un ,password = pw)
        if ATO and ATO.is_active and ATO.is_staff :
            TPO = EmployeeProfile.objects.get(username = ATO)
            if TPO.role == 'Trainer':
                login(request,ATO)
                request.session['traineruser'] = un 
                return redirect('trainer_home')
            return HttpResponse('you are not validate user')
        return HttpResponse('credentials do not match')
    
@trainer_login_required
def trainer_logout(request):
    logout(request) 
    return redirect('trainer_login')
   

