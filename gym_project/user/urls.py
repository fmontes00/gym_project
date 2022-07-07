from django import views
from django.urls import include, path
from . import views

urlpatterns = [
    path("signupuser/", views.signup_user, name="signupuser"),
    path("login/", views.login_user, name="login"),
]
