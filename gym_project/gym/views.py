from operator import ipow
from django.shortcuts import render
from .models import Equipment

def home(request):
    equip = Equipment.objects.all()
    return render(request, 'gym/home.html', {'equip' : equip})










