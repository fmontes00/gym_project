
from django.conf import settings
from django.db import models



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

    days = [("m","Monday"),("t","Tuesday"),("w","Wednesday"),("h","Thursday"),("f", "Friday")]

    title = models.CharField(max_length=50)
    day = models.DateField(choices=days)
    exercises = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title