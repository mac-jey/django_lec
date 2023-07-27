from django.contrib import admin
from .models import MainContent

# Register your models here.
admin.site.register(MainContent)


from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

#Create your views here.
#Signup.
"""def signup(request):
    if request.method == 'POST':
        if request.POST['password1']== request.POST['password2']:
            user =  User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html')
    return render(request,'signup.html')"""