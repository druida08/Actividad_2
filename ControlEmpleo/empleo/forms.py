from django import forms
from .models import Empresa, OfertaEmpleo

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre', 'descripcion']

class OfertaEmpleoForm(forms.ModelForm):
    class Meta:
        model = OfertaEmpleo
        fields = ['titulo', 'empresa', 'salario', 'experiencia', 'nivel_estudio']
