from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Equipment, Exercise, Routine , RoutineBlock


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
        fields = ["title", "day", "routine", "is_completed"]

class RoutineblockForm(ModelForm):
    class Meta:
        model = RoutineBlock
        fields = ["routine", "classification","exercises"]
