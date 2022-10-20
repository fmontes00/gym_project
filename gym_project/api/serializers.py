from dataclasses import field, fields
from rest_framework import serializers
from gym.models import Exercise, Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ("name","description")

class ExerciseSerializer(serializers.ModelSerializer):  # ver permissions para poeder hacer un delete
    class Meta:
        model = Exercise
        fields = ("name","description","equipment")