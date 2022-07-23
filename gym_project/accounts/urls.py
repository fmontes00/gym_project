from django.urls import path, include
from .views import LogoutView2, SignUpView , HomeView, LoginView2

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("home/",HomeView.as_view(), name="home"),
    path("login/",LoginView2.as_view(),name = "login"),
    path("logout/",LogoutView2.as_view(),name = "logout"),
]
