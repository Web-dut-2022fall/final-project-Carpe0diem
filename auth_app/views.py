from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.

def sign_in(request):
    if request.method == 'GET':
        return render(request,'login.html')

    else:

        uname=request.POST['username']
        pwd=request.POST['password']
        user=authenticate(username=uname,password=pwd)
        
        if user :
            login(request,user)
            return redirect('home')

        
        return redirect('login')

def sign_out(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')

    else:
        uname=request.POST['username']
        pwd=request.POST['password']
        user=User.objects.create_user(username=uname,password=pwd)
        user.save()
        return redirect('login')



