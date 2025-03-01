from django.shortcuts import render,redirect
from manager.forms import *
from django.views.generic import View
from django.http import HttpResponse
from django.core.mail import  send_mail
from django.contrib.auth import authenticate,login,logout
from trainer.forms import   * 
import random
# Create your views here.





class ForgetPasswordView(View):
    def get(self,request):
        return render(request,'trainer/forget_password.html')
    def post(self,request):
        username = request.POST.get('username')
        UO = User.objects.get(username = username)
        EPO =EmployeeProfile.objects.get(username = UO)
        # if (UO.is_active and not  UO.is_staff and  EPO.role == 'Trainer') :
        #     return HttpResponse('you are not a Trainer')
        email = UO.email
        otp = str(random.randint(999,10000))
        request.session['forget_user']  = UO.username
        request.session['verify_otp'] = otp 
        print(otp)
        send_mail(
            'otp verification',
            otp,
            'kumarmanoj8260910@gmail.com',
            [email],
            fail_silently=False
        )
        return redirect('tariner_otp_verify')
    
class VerifyOtpView(View):
    def get(self,request):
        return render(request,'trainer/otp_verify.html') 
    def post(self,request):
        enter_otp = request.POST.get('otp')  
        verify_otp  = request.session.get('verify_otp')

        if enter_otp == verify_otp :
            return redirect('trainer_new_password')
        return HttpResponse('invalid otp') 

class NewPasswordView(View):
    def get(self,request):
        return render(request,'trainer/new_password.html') 
    def post(self,request):
        pw1 =  request.POST.get('pw1')
        pw2 =  request.POST.get('pw2')
        un = request.session.get('forget_user')
        UO = User.objects.get(username = un)
        if pw1  == pw2 :
            UO.set_password(pw1)
            UO.save()
            return redirect('trainer_login')
        return HttpResponse('password does not match')




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
   

