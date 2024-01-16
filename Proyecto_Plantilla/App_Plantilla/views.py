""" ------------------------------------------------- App_Plantilla => views """
"""
Vistas de ejemplo para App

- vista_1: uso de plantilla html, método render()
"""

from django.shortcuts import 

# Create your views here.



# ---------------------------------------------------------------------- portada
# Página principal de presentación del proyecto
def portada(request):
    return render(request, 'App_Plantilla/portada.html')



# ---------------------------------------------------------------------- Vista 1
# Página simple de ejemplo para renderizado de html y herencia de platilla base 
def vista_1(request):
    return render(request, 'App_Plantilla/vista_1.html')

    