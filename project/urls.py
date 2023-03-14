"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppFormularios.views import index, mostrar_alumnos, agregar_alumnos, mostrar_profesores, agregar_profesor, mostrar_cursos, agregar_curso, buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('alumnos/', mostrar_alumnos, name="alumnos"),
    path('alumnos/agregar', agregar_alumnos, name="agregar-alumno"),
    path('profesores/', mostrar_profesores, name="profesores"),
    path('profesores/agregar', agregar_profesor, name="agregar-profesor"),
    path('cursos/', mostrar_cursos, name="cursos"),
    path('cursos/agregar', agregar_curso, name="agregar-curso"),
    path('profesores/buscar', buscar, name="buscar"),
]
