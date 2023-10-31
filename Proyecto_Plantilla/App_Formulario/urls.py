""" ------------------------------------------------- App_Formulario => urls """
"""
1- formulario: plantilla de formulario básico
2- formulario_2 : plantilla de formulario secundario
"""

from django.urls import path
from App_Formulario import views

urlpatterns = [
    path('formulario/', views.formulario, name='FORMULARIO'),          # 1   
    path('formulario_2/', views.formulario_2, name='FORMULARIO_2'),    # 2
]