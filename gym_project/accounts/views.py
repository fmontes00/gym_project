from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView , LogoutView
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
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

class LogoutView2(LogoutView):
    template_name = "accounts/base.html"