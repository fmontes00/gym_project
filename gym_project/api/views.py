import ipdb
from .serializers import EquipmentSerializer, ExerciseSerializer
from gym.models import Equipment, Exercise
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, viewsets, generics


class ExerciseViewSet(viewsets.ViewSet):
    def list(self, request):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"detail": "Given payload is invalid"}, status=status.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, pk=None):
        try:
            exercise = Exercise.objects.get(id=pk)
        except Exercise.DoesNotExist:
            return Response(
                {"detail": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            equipment = Exercise.objects.get(id=pk)
        except Exercise.DoesNotExist:
            return Response({"detail": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ExerciseSerializer(equipment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        try:
            equipment = Exercise.objects.get(id=pk)
        except Exercise.DoesNotExist:
            return Response({"detail":"Exercise not found"}, status=status.HTTP_404_NOT_FOUND)
        equipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class EquipmentViewSet(viewsets.ViewSet):
    def list(self, request):
        equipment = Equipment.objects.all()
        serializer = EquipmentSerializer(equipment, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk= None):
        try:
            equipment = Equipment.objects.get(id=pk)
        except Equipment.DoesNotExist:
            return Response({"detail":"Equipment not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data)


    def create(self, request):
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"detail": "Given payload is invalid"}, status=status.HTTP_400_BAD_REQUEST
        )
        

    def update(self, request, pk= None):
        try:
            equipment = Equipment.objects.get(id=pk)
        except Equipment.DoesNotExist:
            return Response({"detail": "Equipment not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EquipmentSerializer(equipment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update():
        pass

    def destroy(self, request, pk=None):
        try:
            equipment = Equipment.objects.get(id=pk)
        except Equipment.DoesNotExist:
            return Response({"detail":"Equipment not found"}, status=status.HTTP_404_NOT_FOUND)
        equipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
































# class EquipmentApiView(generics.ListAPIView):
#     queryset = Equipment.objects.all()
#     serializer_class = EquipmentSerializer


# class ExerciseApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Exercise.objects.all()
#     serializer_class = ExerciseSerializer


# @api_view()
# def equipment_list(request):
#     # agarrar todos los equipments
#     equipments = Equipment.objects.all()
#     # armar lista de equipments

#     serializer = EquipmentSerializer(equipments, many=True).data
#     # deveolver lista de equipments

#     return Response(serializer)


# @api_view()
# def equipment_retrieve(request, pk):
#     ipdb.set_trace()
#     import ipdb

#     ipdb.set_trace()
#     try:
#         equipment = Equipment.objects.get(id=pk)
#     except Equipment.DoesNotExist:
#         return Response({"detail": "Equipment not found"}, status=404)
#     # data = {
#     #     "name": equipment.name,
#     #     "description": equipment.description,
#     # }
#     serializer = EquipmentSerializer(equipment)

#     return Response(serializer.data)


# @api_view(["POST"])
# def create_equipment(request):

#     serializer = EquipmentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)


# @api_view(["PUT"])
# def equipment_edition(request, pk):
#     try:
#         equipment = Equipment.objects.get(id=pk)
#     except Equipment.DoesNotExist:
#         return Response({"detail": "Equipment not found"}, status=404)
#     serializer = EquipmentSerializer(equipment, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["DELETE"])
# def delete_equipment(request, pk):
#     equipment = Equipment.objects.get(id=pk)
#     equipment.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
