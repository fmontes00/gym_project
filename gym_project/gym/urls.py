from django.urls import include, path
from . import views
from .views import HomeView, ExerciseFormView, EquipmentFormView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("createExercise", ExerciseFormView.as_view(), name="create_exercise"),
    path("createEquipment", EquipmentFormView.as_view(), name="create_equipment"),
    path("homepage/",views.homepage, name='homepage'),
]
