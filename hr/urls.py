from django.urls import path
from hr.views import *
urlpatterns =[
    path('',HrHome.as_view(),name='hr_home'),
    path('login',HrLogin.as_view(),name='hr_login'),
    path('logout',hr_logout,name='hr_logout'),
]