from django.shortcuts import render,redirect
from manager.forms import *
from django.views.generic import View
from django.http import HttpResponse
from django.core.mail import  send_mail
from django.contrib.auth import authenticate,login,logout
from hr.models import *
from hr.forms import *
from student.models import StudentProfile
import csv
from django.core.mail import send_mail
import random
import os
from skillgo.settings import EMAIL_HOST_USER
# Create your views here.


def get_student_details(request):
    all_students = User.objects.filter(is_active = True , is_staff = False , is_superuser = False)
    print(all_students)
    # file_path = os.path.join(settings.MEDIA_ROOT,'Student_saved/students_save.csv')
    file_path = 'student_save.csv'

    with open(file_path,'w') as csvfile :
        writer = csv.DictWriter(csvfile,fieldnames=['id' ,'first_name','last_name', 'username','email'])

        writer.writeheader()
        for student in all_students: 
            writer.writerow({
                'id' : student.id,
                'first_name':student.first_name,
                'last_name' :student.last_name,
                'username' :student.username,
                'email' :student.email
            })
            print(file_path)
    d= {'file': csvfile}       

    return render(request,'')

class ForgetPasswordView(View):
    def get(self,request):
        return render(request,'hr/forget_password.html')
    def post(self,request):
        username = request.POST.get('username')
        UO = User.objects.get(username = username)
        EPO =EmployeeProfile.objects.get(username = UO)

        # if (UO.is_active and not  UO.is_staff and  EPO.role == 'Hr' ) :
        #     return HttpResponse('you are not a Hr')
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
        return redirect('hr_otp_verify')
    
class VerifyOtpView(View):
    def get(self,request):
        return render(request,'hr/otp_verify.html') 
    def post(self,request):
        enter_otp = request.POST.get('otp')  
        verify_otp  = request.session.get('verify_otp')

        if enter_otp == verify_otp :
            return redirect('hr_new_password')
        return HttpResponse('invalid otp') 

class NewPasswordView(View):
    def get(self,request):
        return render(request,'hr/new_password.html') 
    def post(self,request):
        pw1 =  request.POST.get('pw1')
        pw2 =  request.POST.get('pw2')
        un = request.session.get('forget_user')
        UO = User.objects.get(username = un)
        if pw1  == pw2 :
            UO.set_password(pw1)
            UO.save()
            return redirect('hr_login')
        return HttpResponse('password does not match')





class SchedulingsView(View):
     def get(self,request):
          ESFO = SchedulingsForm()
          context = {'ESFO':ESFO}
          return render(request,'hr/scheduling_mock.html',context)
     def post(self,request):
          if request.FILES:
               SFDO = SchedulingsForm(request.POST,request.FILES)
               if SFDO.is_valid():
                    SFDO.save()
                    with open(f"media/Slots/{SFDO.cleaned_data.get('trainer').username}_{SFDO.cleaned_data.get('subject')}.csv",'r') as file :
                         reader = csv.reader(file)

                         header = next(reader)
                         username = [line[3] for line in reader]
                         print(username)  
                         for un in username :
                            SO = User.objects.get(username = un)
                            schedule_email = SO.email
                            hrun =request.session.get('hruser')
                            HRO = User.objects.get(username = hrun)
                            HRPO = EmployeeProfile.objects.get(username = HRO)
                            message = f"""
Dear {SO.first_name}  {SO.last_name},

I hope you’re doing well! We are excited to invite you for a mock interview as part of your preparation for the  at [Company Name]. This session is designed to help you practice and receive constructive feedback before your official interview.

Interview Details:
📅 Date: {SFDO.cleaned_data.get('scheduling_date')}
⏰ Time: {SFDO.cleaned_data.get('scheduling_time')}
📍 Location/Platform: QSpiders Bhubaneswar
⏳ Duration: 30min

During the mock interview, we will focus on [mention key topics such as behavioral questions, technical skills, case study, etc.], followed by a feedback session.

Please confirm your availability at your earliest convenience. Feel free to reach out if you have any questions. We look forward to helping you prepare!

Best regards,
{HRO.first_name} {HRO.last_name}
{HRPO.role}
QSpiders Bhubaneswar
Contact : - 8260910585
"""
                         send_mail(
                          'Invitation for Mock Interview – QSpiders Bhubaneswar',
                          message,
                          EMAIL_HOST_USER,
                          [schedule_email],
                          fail_silently=False
                         )
                         
                         return redirect('hr_home')        
               return HttpResponse('invalid')
          return HttpResponse('nofile')
          



class HrHome(View):
    def get(self,request):
        all_ratings= Ratings.objects.all()
     #    students = User.objects.filter(is_active = True)
     #    SPO = StudentProfile.objects.filter(username__in = students)
     #    print(SPO)
     #    print(students)
        all_courses = [course[0] for course in StudentProfile.courses]
        context = {'all_ratings' :all_ratings,'all_courses' : all_courses}
        return render(request,'hr/home.html',context)
    def post(self,request):
         course = request.POST.get('course')
         all_ratings= Ratings.objects.all()
         search_student = StudentProfile.objects.filter(course = course)
         print(search_student)
         all_courses = [course[0] for course in StudentProfile.courses]
         context = {'all_ratings' :all_ratings,'all_courses' : all_courses,'search_student':search_student}
         return render(request,'hr/home.html',context)
         
         
    
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



         