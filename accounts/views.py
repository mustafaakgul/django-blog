from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)  # post olduysa giricek olmadysa yni get olduysa hic girmicek
    if form.is_valid():  # clean fonk cagrlir
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()

        # login(request,newUser)  # automatic login after register
        login(request, newUser)  # automatic login after register
        messages.info(request, "Successful Registration")  # ADD SUCCESS FOR GREEN IF ANY PROBLEM OCCURS
        return redirect("index")  # name olani klnncak
    context = {
        "form": form
    }
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
        /////////////

    form = RegisterForm()
    context = {
        "form" : form
    }
    return render(request, "register.html", context)"""


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)  # db ye bak varmi ykmu

        if user is None:
            messages.info(request, "Username or password is invalid")
            return render(request, "login.html", context)

        messages.success(request, "Successfully login")
        login(request, user)
        return redirect("index")
    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request, "Succesfull Logout")
    return redirect("index")


"""
from django.shortcuts import render
from .forms import RegisterForm,LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

from django.shortcuts import redirect

from django.contrib import messages

# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)  #post olduysa giricek olmadysa yni get olduysa hic girmicek
    if form.is_valid():  # clean fonk cagrlir
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()

        #login(request,newUser)  # automatic login after register
        messages.success(request, "Successful Registration")
        return redirect("index")  # name olani klnncak
    context = {
        "form": form
    }
    return render(request, "register.html", context)


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

def loginUser(request):

    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password) # db ye bak varmi ykmu

        if user is None:
            messages.info(request, "Username or password is invalid")
            return render(request, "login.html", context)

        messages.success(request, "Successfull login")
        login(request, user)
        return redirect("index")
    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Succesfull Logput")
    return redirect("index")
"""


from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('home')

    return render(request, "accounts/form.html", {"form": form, 'title': 'Giriş Yap'})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        # user.is_staff = user.is_superuser = True
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('home')

    return render(request, "accounts/form.html", {"form": form, 'title': 'Üye Ol'})


def logout_view(request):
    logout(request)
    return redirect('home')
