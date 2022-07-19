from django.forms import ModelForm
from .models import Equipment, Exercise


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ["name", "description", "equipment"]


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ["name", "description"]
