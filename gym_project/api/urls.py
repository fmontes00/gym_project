from django.urls import path
from .views import EquipmentApiView, ExerciseApiView , equipment_list, equipment_retrieve


urlpatterns = [

    #path("equipments/",EquipmentApiView.as_view(), name="equipment_list"),
    path("exercises/<int:pk>",ExerciseApiView.as_view(), name="exercise_retrieve"),
    path("equi/",equipment_list,name="equi"),
    path("eq/<int:pk>",equipment_retrieve,name="eq"),
]