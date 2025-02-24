from django.urls import path
from manager.views import *
urlpatterns=[
   path('',ManagerHome.as_view(),name='manager_home'),
   path('add_emp',AddEmployee.as_view(),name='add_employee'),
   path('login',ManagerLogin.as_view(),name='manager_login'),
   path('logout',manager_logout,name='manager_logout'),
]