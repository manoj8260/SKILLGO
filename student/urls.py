from  django.urls import path
from  student.views import *

urlpatterns =[
     path('',StudentHome.as_view(),name="student_home"),
     path('register/',StudentRegister.as_view(),name='student_register'),
     path('login/',StudentLogin.as_view(),name='student_login'),
     path('login/',StudentLogin.as_view(),name='student_login'),
     path('logout/',StudentLogout.as_view(),name='student_logout'),
]