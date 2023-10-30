""" ------------------------------------------------- App_Formulario => urls """
"""
1- formulario: plantilla de formulario básico
"""

from django.urls import path
from App_Formulario import views

urlpatterns = [
    path('formulario/', views.formulario, name='FORMULARIO'),   # 1        
]