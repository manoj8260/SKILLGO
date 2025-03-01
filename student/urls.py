from  django.urls import path
from  student.views import *

urlpatterns =[
     path('',StudentHome.as_view(),name="student_home"),
     path('register/',StudentRegister.as_view(),name='student_register'),
     path('login/',StudentLogin.as_view(),name='student_login'),
     path('login/',StudentLogin.as_view(),name='student_login'),
     path('logout/',StudentLogout.as_view(),name='student_logout'),
     path('forget_password/',ForgetPasswordView.as_view(),name='stu_forget_password'),
     path('otp_verify/',VerifyOtpView.as_view(),name='stu_otp_verify'),
     path('new_password/',NewPasswordView.as_view(),name='stu_new_password'),

]