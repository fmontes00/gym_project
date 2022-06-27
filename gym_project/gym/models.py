from django.db import models

# Create your models here.


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)





