from pyexpat import model
from turtle import title
from django.conf import settings
from django.db import models
from gym_project import settings


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
    title = models.CharField(max_length=200)
    day = models.CharField(max_length=100)
    content = models.TextField()
    is_completed = models.BooleanField(default=False)
    user = models.ManyToManyField("accounts.CustomUser")

    def __str__(self):
        return self.title

class RoutineBlock(models.Model):
    METCON = "mc"
    AMRAP ="am"
    TABATA = "tb"
    OTM = "ot"

    routine_type_choices = [
        (METCON, "Metcon"),
        (AMRAP, "Amrap"),
        (TABATA, "Tabata"),
        (OTM, "OTM"),
    ]

    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
   # order = ver django-ordered-model
    exercises = models.ManyToManyField(Exercise)
    classification = models.CharField(choices=routine_type_choices)

