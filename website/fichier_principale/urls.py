from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('aide', views.aide, name='aide'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('information/', views.information, name='information'),
    path('service/', views.service, name='service'),


    path('impot/', views.impot, name='impot'),
    
    
    path('login/', views.login, name='login'),
    path('signup1/', views.signup1, name='signup1'),
]