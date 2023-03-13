from django.shortcuts import render
from AppFormularios.models import Alumno
from AppFormularios.forms import AlumnoForm

# Create your views here.

def index(request):
    return render(request, "AppFormularios/index.html")

def otro(request):
    return render(request, "AppFormularios/otro.html")

def mostrar_alumnos(request):
    context = {
        "form": AlumnoForm(),
        "alumnos": Alumno.objects.all(),
    }
    return render(request, "AppFormularios/admin_alumnos.html", context)

def agregar_alumnos(request):
    alumno_form= AlumnoForm(request.POST)
    alumno_form.save()
    context = {
        "alumnos": Alumno.objects.all(),
        "form": AlumnoForm(),
    }
    return render(request, "AppFormularios/admin_alumnos.html", context)

def buscar_alumno(request):
    criterio = request.GET.get("criterio")
    context = {
        "alumnos": Alumno.objects.filter(nombre__icontains=criterio).all()
    }
    return render(request, "AppFormularios/admin_alumnos.html", context)
