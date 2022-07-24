from django.views import View
from django.shortcuts import redirect, render
from .models import Equipment, Routine
from .forms import EquipmentForm, ExerciseForm, RoutineForm
from django.views.generic import TemplateView
from django.views.generic.edit import FormView


# Create your views here.


# def home(request):
#     equipments = Equipment.objects.all()
#     return render(request, "gym/home.html", {"equipments": equipments})


class HomeView(View):
    def get(self, request):
        equipments = Equipment.objects.all()
        routines = Routine.objects.all()
        return render(request, "gym/home.html", {"equipments": equipments, "routines":routines})


def homepage(request):
    return render(request, "gym/homepage.html")


# class HomeView(TemplateView):
#     template_name = "gym/home.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["equipments"] = Equipment.objects.all()
#         return context


# class ExerciseFormView(FormView):
#     template_name = "gym/create_exercise.html"
#     form_class = ExerciseForm
#     success_url = "/gym"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class ExerciseFormView(View):

    form_class = ExerciseForm

    def get(self, request):
        form = self.form_class
        return render(request, "gym/create_exercise.html", {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)  # ExerciseForm(request.POST)
        form.save()
        return redirect("home")


# def create_exercise(request):
#     if request.method == "GET":
#         form = ExerciseForm()
#         return render(request, "gym/create_exercise.html", {"form": form})
#     else:
#         form = ExerciseForm(request.POST)
#         form.save()
#         return redirect("home")


# class EquipmentFormView(FormView):
#     template_name = "gym/create_equipment.html"
#     form_class = EquipmentForm
#     success_url = "/gym"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class EquipmentFormView(View):

    form_class = EquipmentForm

    def get(self, request):
        form = self.form_class
        return render(request, "gym/create_equipment.html", {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        form.save()
        return redirect("home")


# def create_equipment(request):
#     if request.method == "GET":
#         form = EquipmentForm()
#         return render(request, "gym/create_equipment.html", {"form": form})
#     else:
#         form = EquipmentForm(request.POST)
#         form.save()
#         return redirect("home")


# def create_routine(request):
#     if request.method == 'GET':
#         routine_form = RoutineForm()
#         return render(request, "gym/create_routine.html", {"routine_form" : routine_form})
#     else:
#         routine_form = RoutineForm(request.POST)
#         new_routine_form = routine_form.save(commit=False)
#         new_routine_form.save()
#         return redirect("myroutine")


# class EquipmentFormView(FormView):
#     template_name = "gym/create_equipment.html"
#     form_class = EquipmentForm
#     success_url = "/gym"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class RoutineFormView(FormView):
    template_name = "gym/create_routine.html"
    form_class = RoutineForm
    success_url = "/gym"

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return super().form_valid(form)


    # def get_initial(self):
    #     initial = super(RoutineFormView, self).get_initial()
    #     if self.request.user.is_authenticated:
    #         initial.update({'user': self.request.user})
    #     return initial
