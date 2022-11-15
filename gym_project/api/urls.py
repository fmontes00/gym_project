from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EquipmentApiView,
    ExerciseApiView,
    equipment_list,
    equipment_retrieve,
    equipment_edition,
    create_equipment,
    delete_equipment,
    ExerciseViewSet,
)


router = DefaultRouter(trailing_slash = False)
router.register(r'exercises', ExerciseViewSet, basename='exercise')

urlpatterns = [
    # path("equipments/",EquipmentApiView.as_view(), name="equipment_list"),
    #path("exercises", ExerciseViewSet, name="exercises"),
    path("equi/", equipment_list, name="equi"),
    path("", include(router.urls))
    # path("eq/<int:pk>", equipment_retrieve, name="eq"),
    # path("edit/<int:pk>", equipment_edition, name="edit"),
    # path("create", create_equipment, name="create"),
    # path("delete/<int:pk>", delete_equipment, name="delete"),
]
