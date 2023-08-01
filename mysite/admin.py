from django.contrib import admin
from .models import MainContent

# Register your models here.
admin.site.register(MainContent)


from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

#Create your views here.
