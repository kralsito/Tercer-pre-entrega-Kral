from django.shortcuts import render
from AppFormularios.models import Alumno, Profesor, Curso
from AppFormularios.forms import AlumnoForm, ProfesorForm, CursoForm

# Create your views here.

def index(request):
    return render(request, "AppFormularios/index.html")

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

def mostrar_profesores(request):
    context = {
        "form": ProfesorForm(),
        "profesores": Profesor.objects.all(),
    }
    return render(request, "AppFormularios/admin_profesores.html", context)

def agregar_profesor(request):
    profesor_form= ProfesorForm(request.POST)
    profesor_form.save()
    context = {
        "profesores": Profesor.objects.all(),
        "form": ProfesorForm(),
    }
    return render(request, "AppFormularios/admin_profesores.html", context)


def mostrar_cursos(request):
    context = {
        "form": CursoForm(),
        "cursos": Curso.objects.all(),
    }
    return render(request, "AppFormularios/admin_cursos.html", context)

def agregar_curso(request):
    curso_form= CursoForm(request.POST)
    curso_form.save()
    context = {
        "cursos": Curso.objects.all(),
        "form": CursoForm(),
    }
    return render(request, "AppFormularios/admin_Cursos.html", context)

def buscar(request): #Modificar
    criterio = request.GET.get("criterio")
    context = {
        "profesores": Profesor.objects.filter(nombre__icontains=criterio).all(),
        "alumnos": Alumno.objects.filter(nombre__icontains=criterio).all(),
        "cursos": Curso.objects.filter(nombre__icontains=criterio).all(),
    }
    return render(request, "AppFormularios/busqueda.html", context)


