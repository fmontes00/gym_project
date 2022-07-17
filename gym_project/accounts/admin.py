from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import UserForm


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = UserForm

    #fields = (*UserAdmin.fieldsets,)


admin.site.register(User)


# Register your models here.
