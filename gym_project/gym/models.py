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
    LUNES = "lu"
    MARTES = "ma"
    MIERCOLES = "mi"
    JUEVES = "ju"
    VIERNES = "vi"

    day_choices = [
        (LUNES, "lunes"),
        (MARTES, "martes"),
        (MIERCOLES, "miercoles"),
        (JUEVES, "jueves"),
        (VIERNES, "viernes"),
    ]

    title = models.CharField(max_length=200)
    day = models.CharField(max_length=100, choices=day_choices)
    content = models.TextField()
    is_completed = models.BooleanField(default=False)
    user = models.ManyToManyField("accounts.CustomUser")

    def __str__(self):
        return self.title


class RoutineBlock(models.Model):
    METCON = "mc"
    AMRAP = "am"
    TABATA = "tb"
    OTM = "ot"

    BLOCK1 = "b1"
    BLOCK2 = "b2"
    BLOCK3 = "b3"

    routine_type_choices = [
        (METCON, "Metcon"),
        (AMRAP, "Amrap"),
        (TABATA, "Tabata"),
        (OTM, "OTM"),
    ]

    routine_block_choices = [
        (BLOCK1, "block 1"),
        (BLOCK2, "block 2"),
        (BLOCK3, "block 3"),
    ]

    name = models.CharField(max_length=100, choices=routine_block_choices)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    # order = ver django-ordered-model
    exercises = models.ManyToManyField(Exercise)
    classification = models.CharField(max_length=200, choices=routine_type_choices)

    def __str__(self):
        return self.name
