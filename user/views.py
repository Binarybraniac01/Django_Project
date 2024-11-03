from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *


# @login_required(login_url="/login-page/")

def register_page(request):

    if request.method == "POST":
        data = request.POST

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists. Please use another username...")
            return redirect('/register-page/')

        user = User.objects.create(first_name=first_name, 
                                   last_name=last_name,
                                   username=username)
        
        user.set_password(password)
        user.save()
        messages.info(request, "User registration successfull.....")
        return redirect('/register-page/')

    return render(request, "register.html", context={"page": "Register"})



def login_page(request):

    if request.method == "POST":
        data = request.POST

        username = data.get("username")
        password = data.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username...")
            return redirect('/login-page/')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid Password...")
            return redirect('/login-page/')
        else:
            login(request, user)
            return redirect("/")

    return render(request, "login.html", context={"page": "Login"})


@login_required(login_url="/login-page/")
def logout_view(request):
    logout(request)
    return redirect('/login-page/')



