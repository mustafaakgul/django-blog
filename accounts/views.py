from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def register(request):
    form = RegisterForm(request.POST or None)  # post olduysa giricek olmadysa yni get olduysa hic girmicek
    context = {
        "form": form
    }
    if form.is_valid():  # Calling Clean Method
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = User(username=username)
        user.set_password(password)
        user.save()

        #new_user = authenticate(username=user.username, password=password)
        login(request, user)  # Automatically Login
        messages.info(request, "Registration Successful")  # ADD SUCCESS FOR GREEN IF ANY PROBLEM OCCURS
        return redirect("index")

    return render(request, "register.html", context)


    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():  #clean fonk cagrlir
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()

            login(request, newUser)     #automatic login after register
            return redirect("index")           #name olani klnncak
        context = {
            "form": form
        }
        return render(request, "register.html", context)
    else:
        form = RegisterForm()
        context = {
            "form" : form
        }
        return render(request, "register.html", context)

    form = RegisterForm()
    context = {
        "form" : form
    }
    return render(request, "register.html", context)
    """


def login(request):

    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)  # DB Look Up

        if user is None:
            messages.info(request, "Username or password is invalid")
            return render(request, "login.html", context)

        messages.success(request, "Login Successful")
        login(request, user)
        return redirect("index")

    return render(request, "login.html", context)


def logout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect("index")
