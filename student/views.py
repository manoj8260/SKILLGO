from django.shortcuts import render,redirect
from django.views.generic import View
from student.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.


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




                

 

