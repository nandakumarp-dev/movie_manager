from django.shortcuts import render

# Create your views here.

from django.views import View


class WelcomeView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'welcome/welcome_page.html')
    
class SignupView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'welcome/signup.html')
    
class LoginView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'welcome/login.html')