from django.shortcuts import render,redirect
from django.views import View
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import *

# Create your views here.
class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'login.html',{"form":form})
    def post(self,request):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pword=form_data.cleaned_data.get('password')
            # here we gone verify with saved data
            user=authenticate(request,username=uname,password=pword)
            print(user)

            if user:
                login(request,user)
                messages.success(request,'Login successful')
                return redirect('tlist')
            else:
                messages.error(request,'Login Failed.Inavalide Username/Password')
                return redirect('log')
        else:
            return render(request,'login.html',{"forms":form_data})

class RegView(View):
    def get(self,request):
        form=RegForm()
        return render(request,'reg.html',{'form':form})
    def post(self,request):
        form_data=RegForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"User registration successful")
            return redirect('log')
        else:
            messages.error(request,"User registration failed")
            return render(request,'login.html',{'form':form_data})
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('log')