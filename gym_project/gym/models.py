
#from django.conf import settings
from django.conf import settings
from django.db import models
from gym_project import settings
from accounts.models import User


# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    equipment = models.ForeignKey("gym.Equipment", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Routine(models.Model):

    title = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    exercises = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title