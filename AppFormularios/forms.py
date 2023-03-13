from django import forms 
from AppFormularios.models import Alumno, Profesor, Curso

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'