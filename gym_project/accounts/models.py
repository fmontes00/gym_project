from ast import arg
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    is_athlete = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
