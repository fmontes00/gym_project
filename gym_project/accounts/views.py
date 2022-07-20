from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView , TemplateView
from .forms import CustomUserCreationForm



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    succes_url = reverse_lazy("home")
    template_name = "accounts/signup.html"



class HomeView(TemplateView):
    def get(self, request):
        return render(request, "accounts/home.html")
