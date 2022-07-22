from django.urls import path, include
from .views import SignUpView , HomeView, LoginView2

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("home/",HomeView.as_view(), name="home"),
    path("login/",LoginView2.as_view(),name = "login"),
]
