from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.forms import UserForm, AuthForm
from django.contrib.auth import login, logout, authenticate
from .models import User

# Create your views here.


def signup_user(request):
    if request.method == "GET":
        return render(request, "accounts/signupuser.html", {"form": UserForm()})
    else:
        if request.POST["password"] :
            try:
                user = User.objects.create_user(
                    username=request.POST["email"],
                    password=request.POST["password"],
                )
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(
                    request,
                    "accounts/signupuser.html",
                    {
                        "form": UserForm(),
                        "error": "username alredy taken, select a new one",
                    },
                )
        else:
            return render(
                request,
                "accounts/signupuser.html",
                {"form": UserForm(), "error": "passwords did not match"},
            )


def login_user(request):
    if request.method == "GET":
        return render(request, "accounts/login.html", {"form": AuthForm()})
    else:
        user = authenticate(
            request,
            username=request.POST["email"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "accounts/login.html",
                {
                    "form": AuthForm(),
                    "error": "username and password did not match",
                },
            )
        else:
            login(request, user)
            return redirect("createRoutine")

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')


# Create your views here.
