from django.shortcuts import render,redirect
from django.views.generic import View
from student.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
import random


# Create your views here.

class ForgetPasswordView(View):
    def get(self,request):
        return render(request,'student/forget_password.html')
    def post(self,request):
        username = request.POST.get('username')
        UO = User.objects.get(username = username)
        # if (UO.is_active and  UO.is_staff ) :
        #     return HttpResponse('you are not a student')
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
        return redirect('stu_otp_verify')
    
class VerifyOtpView(View):
    def get(self,request):
        return render(request,'student/otp_verify.html') 
    def post(self,request):
        enter_otp = request.POST.get('otp')  
        verify_otp  = request.session.get('verify_otp')

        if enter_otp == verify_otp :
            return redirect('stu_new_password')
        return HttpResponse('invalid otp') 

class NewPasswordView(View):
    def get(self,request):
        return render(request,'student/new_password.html') 
    def post(self,request):
        pw1 =  request.POST.get('pw1')
        pw2 =  request.POST.get('pw2')
        un = request.session.get('forget_user')
        UO = User.objects.get(username = un)
        if pw1  == pw2 :
            UO.set_password(pw1)
            UO.save()
            return redirect('student_login')
        return HttpResponse('password does not match')




def upload_resume(request):
    pass

class StudentHome(View):
    def get(self,request):
        return render(request,'student/home.html')

class StudentRegister(View):
    def get(self,request):
        studUserFormObj = StudentUserForm()
        studProfileObj = StudentProfileForm()
        context = {'studUserFormObj':studUserFormObj,'studProfileObj':studProfileObj}
        return render(request,'student/register.html',context)
    def post(self,request):
        if request.FILES : 
            SUFDO = StudentUserForm(request.POST)
            SPFDO = StudentProfileForm(request.POST,request.FILES)
            if SUFDO.is_valid() and SPFDO.is_valid():
                MSUFDO = SUFDO.save(commit=False)
                MSUFDO.set_password(SUFDO.cleaned_data.get('password'))
                MSPFDO = SPFDO.save(commit=False)
                MSPFDO.username = MSUFDO
                MSUFDO.save()
                MSPFDO.save()
                return redirect('student_login')
            return HttpResponse('invalid data')
        return HttpResponse('no file ')
    
class StudentLogin(View):
    def  get(self,request):
        return render(request,'student/login.html')  
    
    def post(self,request):
        un = request.POST.get('username')
        pw = request.POST.get('password')
        authenticate_user = authenticate(username = un ,password = pw)
        if authenticate_user and authenticate_user.is_active:
            login(request,authenticate_user)
            request.session['username'] = un
            return  redirect('student_home')
        return HttpResponse('Invalid Credentials')

class StudentLogout(View):
    def get(self,request):
        logout(request)
        return  redirect('student_login')




                

 

