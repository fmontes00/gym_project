from django.shortcuts import render
from .models import Equipment

# Create your views here.



def home(request):
    equipments = Equipment.objects.all()
    return render(request, "gym/home.html", {"equipments": equipments})
