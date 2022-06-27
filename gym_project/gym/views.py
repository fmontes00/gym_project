from operator import ipow
from django.shortcuts import render
from .models import Equipment, Exercise

# def home(request):
#     equipments = Equipment.objects.all()
#     exercises = Exercise.objects.all()
#     return render(request, 'gym/home.html', {'equipments' : equipments, 'exercises' : exercises})


def home(request):
    equipments = Equipment.objects.all()
    return render(request, 'gym/home.html', {'equipments' : equipments})









