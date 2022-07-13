from dataclasses import fields
from pyexpat import model
from statistics import mode
from django.forms import ModelForm
from .models import Equipment, Exercise, Routine


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ["name", "description", "equipment"]


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ["name", "description"]


class RoutineForm(ModelForm):
    class Meta:
        model = Routine
        fields = ["title","day","exercises", "completed"]