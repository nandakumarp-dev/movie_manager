from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('welcome/',views.WelcomeView.as_view(),name='welcome_page'),

    path('signup',views.SignupView.as_view(),name='signup_page'),

    path('login',views.LoginView.as_view(),name='login_page')

]