from django.urls import path
from .views import EquipmentApiView


urlpatterns = [

    path("equipment_api/",EquipmentApiView.as_view(), name="equipment_list"),

]