from django.urls import path
from hr.views import *
urlpatterns =[
    path('',HrHome.as_view(),name='hr_home'),
    path('login/',HrLogin.as_view(),name='hr_login'),
    path('logout/',hr_logout,name='hr_logout'),
    path('mockschedule/',SchedulingsView.as_view(),name='mock_schedule'),
    path('forget_password/',ForgetPasswordView.as_view(),name='hr_forget_password'),
    path('otp_verify/',VerifyOtpView.as_view(),name='hr_otp_verify'),
    path('new_password/',NewPasswordView.as_view(),name='hr_new_password'),
    path('student_deatils/',get_student_details,name='get_all_student'),
]