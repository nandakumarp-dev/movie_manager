from django.urls import path
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('welcome/',views.WelcomeView.as_view(),name='welcome_page'),

    path('signup',views.SignupView.as_view(),name='signup_page'),

    path('login',views.LoginView.as_view(),name='login_page'),

    path('home',views.HomeView.as_view(),name='home_page'),

    path('logout/',LogoutView.as_view(next_page='login_page'),name='logout'),
    
]
