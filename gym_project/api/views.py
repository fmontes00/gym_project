from urllib.request import Request
from .serializers import EquipmentSerializer, ExerciseSerializer
from rest_framework import generics
from gym.models import Equipment, Exercise
from rest_framework.response import Response
from rest_framework.decorators import api_view

class EquipmentApiView(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class ExerciseApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

@api_view()
def equipment_list(request):
    # agarrar todos los equipments
    equipments = Equipment.objects.all()
    # armar lista de equipments

    serializer = EquipmentSerializer(equipments, many = True).data
    # deveolver lista de equipments     

    return Response(serializer)

@api_view()
def equipment_retrieve(request, pk):
    try:
        equipment = Equipment.objects.get(id=pk)
    except Equipment.DoesNotExist:
        return Response({"detail": "Equipment not found"}, status=404)
    # data = {
    #     "name": equipment.name,
    #     "description": equipment.description,
    # }
    serializer = EquipmentSerializer(equipment)

    return Response(serializer.data)


# Create your views here.
