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
        fields = ["title", "day", "routine", "is_completed"]
