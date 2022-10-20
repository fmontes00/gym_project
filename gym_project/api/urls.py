from django.urls import path
from .views import EquipmentApiView, ExerciseApiView


urlpatterns = [

    path("equipment_api/",EquipmentApiView.as_view(), name="equipment_list"),
    path("exercise_api/<int:pk>",ExerciseApiView.as_view(), name="exercise_list"),
]