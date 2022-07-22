from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView   
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView , TemplateView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "accounts/signup.html"



class HomeView(TemplateView):
    def get(self, request):
        return render(request, "accounts/home.html")


class LoginView2(LoginView):
    template_name = "accounts/login.html"