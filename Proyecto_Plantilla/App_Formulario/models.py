""" ----------------------------------------------- App_Formulario => models """
"""
Modelos:
- Formulario: tabla para farmulario plantilla de campos comunes
- Formularios: tabla com campos de imagen,contraseñas y checkbox
"""

from django.db import models

# Create your models here.


# ------------------------------------------------------------------- Formulario
# Modelo de tabla para formulario de campps comunes

class Formulario(models.Model):
    # ----------------------------------------------- campos de texto
    nombre_usuario = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    # ---------------------------------------------- campos numéricos
    edad = models.PositiveIntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.FloatField()

    # ----------------------------------------------- campos de fecha
    fecha_nacimiento = models.DateField()
    ultimo_login = models.DateTimeField(auto_now=True)

    # ---------------------------------------------- campos booleanos
    esta_activa = models.BooleanField(default=True)
    es_personal = models.BooleanField(default=False)

    # ---------------------------------- campos con lista de opciones
    OPCIONES_ROL = [
        ('usuario', 'Usuario_normal'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')



# ----------------------------------------------------------------- Formulario_2
# Modelo de tabla con campo de imagen y contraseñas

class Formulario_2(models.Model):

    usuario = models.CharField(max_length=50, unique=True)
    
    # ----------------------------------------------- Campo de Imagen
    foto = models.ImageField(upload_to="App_Formulario", null=True, blank=True)
    
    # ----------------------------------------- Campos de contraseñas
    password_1 = models.CharField(max_length=50)
    password_2 = models.CharField(max_length=50)
    
    # -------------------------------------------- Campos de checkbox
    suscrito = models.BooleanField(default=False)