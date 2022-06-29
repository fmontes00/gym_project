from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("createExercise", views.create_exercise, name="create_exercise"),
    path("createEquipment", views.create_equipment, name="create_equipment"),
]
