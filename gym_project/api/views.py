from .serializers import EquipmentSerializer, ExerciseSerializer
from rest_framework import generics
from gym.models import Equipment, Exercise

class EquipmentApiView(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class ExerciseApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


# Create your views here.
