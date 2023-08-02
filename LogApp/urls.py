
from django.urls import path
from LogApp import views

urlpatterns = [
    
    path('login', views.login_request, name='Login'),
    
]