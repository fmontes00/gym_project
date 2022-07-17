from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from gym.models import Routine

# Create your models here.


class User(AbstractUser):
    routine = models.ForeignKey(Routine, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


