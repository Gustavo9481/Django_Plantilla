""" ------------------------------------------------ App_Formulario => forms """
"""
Formularios:
- FormularioForm: campos comunes, model => Formulario
- Formulario_2Form: campos imagen, contraseñas y checkbox, model => Formulario_2
"""

from django import forms
from . models import Formulario, Formulario_2


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



# ------------------------------------------------------------- Formulario_2Form
# formulario plantilla con campos de imagen, contraseñas y checkbox

class Formulario_2Form(forms.ModelForm):
    class Meta:
        model = Formulario_2
        fields = [
            'usuario',
            'foto',
            'password_1',
            'password_2',
            'suscrito'
        ]
