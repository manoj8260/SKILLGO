from django.urls import path
from trainer.views import *
urlpatterns =[
    path('',TrainerHome.as_view(),name='trainer_home'),
    path('login/',TrainerLogin.as_view(),name='trainer_login'),
    path('logout/',trainer_logout,name='trainer_logout'),
    path('ratting/',StartMock.as_view(),name='start_mock'),
    path('forget_password/',ForgetPasswordView.as_view(),name='trainer_forget_password'),
    path('otp_verify/',VerifyOtpView.as_view(),name='tariner_otp_verify'),
    path('new_password/',NewPasswordView.as_view(),name='trainer_new_password'),
]