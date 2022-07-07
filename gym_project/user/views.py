from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def signup_user(request):
    if request.method == "GET":
        return render(request, "user/signupuser.html", {"form": UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(
                    request,
                    "user/signupuser.html",
                    {
                        "form": UserCreationForm(),
                        "error": "username alredy taken, select a new one",
                    },
                )
        else:
            return render(
                request,
                "user/signupuser.html",
                {"form": UserCreationForm(), "error": "passwords did not match"},
            )


def login_user(request):
    if request.method == "GET":
        return render(request, "user/login.html", {"form": AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "user/login.html",
                {
                    "form": AuthenticationForm(),
                    "error": "username and password did not match",
                },
            )
        else:
            login(request, user)
            return redirect("home")
