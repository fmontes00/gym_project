from django.contrib import admin
from .models import Exercise, Equipment, Routine, RoutineBlock


# Register your models here.

admin.site.register(Exercise)
admin.site.register(Equipment)
admin.site.register(Routine)
admin.site.register(RoutineBlock)
