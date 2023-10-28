""" -------------------------------------------------- App_Plantilla => urls """
"""
1- portada: página de presentación del proyecto
2- vista_1: uso de plantilla html, método render()
"""

from django.urls import path
from App_Plantilla import views

urlpatterns = [
    path('', views.portada, name='PORTADA'),           # 1
    path('vista_1/', views.vista_1, name='VISTA_1'),   # 2
]