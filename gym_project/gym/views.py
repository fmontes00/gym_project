from django.shortcuts import redirect, render
from .models import Equipment
from .forms import  EquipmentForm, ExerciseForm

# Create your views here.



def home(request):
    equipments = Equipment.objects.all()
    return render(request, "gym/home.html", {"equipments": equipments})


def create_exercise(request):
    if request.method == 'GET':
        form = ExerciseForm()
        return render(request, 'gym/create_exercise.html', {'form' : form})
    else:
        form = ExerciseForm(request.POST)
        form.save()
        return redirect('home')

def create_equipment(request):
    if request.method == 'GET':
        form = EquipmentForm()
        return render(request, 'gym/create_equipment.html', {'form' : form})
    else:
        form = EquipmentForm(request.POST)
        form.save()
        return redirect('home')