from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ExerciseViewSet,
    EquipmentViewSet,
)


router = DefaultRouter(trailing_slash=False)
router.register(r"exercises", ExerciseViewSet, basename="exercise")
router.register(r"equipments",EquipmentViewSet, basename="equipment")

urlpatterns = [
    # path("equipments/",EquipmentApiView.as_view(), name="equipment_list"),
    # path("exercises", ExerciseViewSet, name="exercises"),
    #path("equi/", equipment_list, name="equi"),
    path("", include(router.urls))
    # path("eq/<int:pk>", equipment_retrieve, name="eq"),
    # path("edit/<int:pk>", equipment_edition, name="edit"),
    # path("create", create_equipment, name="create"),
    # path("delete/<int:pk>", delete_equipment, name="delete"),
]
