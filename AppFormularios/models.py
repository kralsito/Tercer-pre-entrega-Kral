from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.IntegerField()
    legajo=models.IntegerField()
    email=models.EmailField()
    def __str__(self):
        return f"{self.id} - {self.nombre}  {self.apellido}"
    
class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.IntegerField()
    legajo=models.IntegerField()
    email=models.EmailField()
    profesion=models.CharField(max_length=30)
    def __str__(self):
        return f"{self.id} - {self.nombre}  {self.apellido}"

class Curso(models.Model):
    nombre=models.CharField(max_length=30)
    año_lectivo=models.IntegerField()
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.año_lectivo}"
    