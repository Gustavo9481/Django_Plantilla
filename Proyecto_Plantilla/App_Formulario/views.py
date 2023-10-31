""" ------------------------------------------------ App_Formulario => views """
"""
Vistas:

- formulario: plantilla de formulario básico
  model=> Formulario | form=> FormularioForm 

- formulario_2: plantilla de formulario secundario
  model=> Formulario_2 | form=> Formulario_2Form
"""

from django.shortcuts import render
from . forms import FormularioForm, Formulario_2Form

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




# ----------------------------------------------------------------- formulario_2
# Página para formulario secundario para imagen, contraseñas y checkbox

def formulario_2(request):
    if request.method == 'POST':
        form = Formulario_2Form(request.POST)
        if form.is_valid():
            form.save()
            # acción o que se hará con los datos del formulario
        else:
            form = Formulario_2Form()

    return render(request, 'App_Formulario/formulario_2.html')
