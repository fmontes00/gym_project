from dataclasses import field, fields
from rest_framework import serializers
from gym.models import Exercise, Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ("name","description")