from django.urls import path, include
from .views import SignUpView, HomeView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("home/", HomeView.as_view(), name="home"),
]
