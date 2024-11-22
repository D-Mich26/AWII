from django import forms
from .models import Empleado, Tecnico, Peticion

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'puesto', 'area']

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['nombre', 'puesto']

class PeticionForm(forms.ModelForm):
    class Meta:
        model = Peticion
        fields = ['descripcion', 'prioridad', 'area', 'fecha', 'empleado_peticion', 'imagen']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'class': 'form-control'})