from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from datetime import datetime
from home.models import Contact
from .forms import UsersignForm
from django.contrib import messages
# Create your views here.
def index(request):    
    return render(request,'index.html')

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date= datetime.today())
        contact.save()
        messages.add_message(request,messages.SUCCESS,'your data has been saved!!!')
     
    return render(request,"contact.html")       

def services(request):
    return render(request,"services.html")  


def sign_up(request):
    if request.method=='POST':
        fm=UsersignForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'User account has been created!!!')
    else:
        fm=UsersignForm()
    return render(request,"signup.html",{'form':fm})    


#login
def user_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username'] 
            pwd=fm.cleaned_data['password'] 
            user=authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect("/profile/")
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'form':fm})

def user_profile(request):
    us=User.objects.all()
    if request.user.is_authenticated:
        return render(request,'profile.html',{'user':us}) 
    else:
        return HttpResponseRedirect("/login/")    


def user_logout(request):
    logout(request)
    return  HttpResponseRedirect("/login/")
                            
