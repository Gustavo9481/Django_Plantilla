""" ------------------------------------------------ App_Formulario => views """
"""
Vistas:

- formulario: plantilla de formulario básico
  model=> Formulario | form=> FormularioForm 
"""

from django.shortcuts import render
from . forms import FormularioForm

# Create your views here.


# ------------------------------------------------------------------- formulario
# Página para formulario básico con campos comunes
def formulario(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            # acción o que se hará con los datos del formulario
        else:
            form = FormularioForm()

    return render(request, 'App_Formulario/formulario.html')