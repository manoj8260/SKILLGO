from django.urls import path
from trainer.views import *
urlpatterns =[
    path('',TrainerHome.as_view(),name='trainer_home'),
    path('login/',TrainerLogin.as_view(),name='trainer_login'),
    path('logout/',trainer_logout,name='trainer_logout'),
    path('ratting/',StartMock.as_view(),name='start_mock'),
]