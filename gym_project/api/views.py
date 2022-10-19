from .serializers import EquipmentSerializer
from rest_framework import generics
from gym.models import Equipment, Exercise

class EquipmentApiView(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


# Create your views here.
