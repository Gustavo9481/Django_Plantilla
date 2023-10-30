""" ------------------------------------------------ App_Formulario => forms """
"""
Formularios:
- FormularioForm: campos comunes, model => Formulario
"""

from django import forms
from . models import Formulario


# --------------------------------------------------------------- FormularioForm
# formulario plantilla con campos básicos, plantilla formulario.html

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = [
            'nombre_usuario',
            'nombre',
            'apellido',
            'email',
            'edad',
            'peso',
            'altura',
            'fecha_nacimiento',
            'roles'
        ]
