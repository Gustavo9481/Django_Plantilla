""" ------------------------------------------------ App Plantilla => models """
"""
Tablas para bases de datos

Modelos (Tablas):
    - Usuarios
    - Usuarios_2
"""

from django.db import models

# Create your models here.

# ------------------------------------------------------------ Tabla Usuarios ☑️
# esquema de la tabla:
# | nombre | apellido | edad | email | nacimiento | adulto | 

class Usuarios(models.Model):
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    edad = models.IntegerField()
    email = models.EmailField()
    nacimiento = models.DateField(verbose_name='fecha de nacimiento')   
    adulto = models.BooleanField()

    # verbose_name = cambia la manera de mostrar el titulo del campo en admin

    def __str__(self):
        # este método permite mostrar la información en el panel de administración
        return f"nombre: {self.nombre} | apellido: {self.apellido} | \
            edad: {self.edad} | email: {self.email} | \
            fecha de nacimiento: {self.nacimiento} | mayor de edad: {self.adulto}"

    

# ---------------------------------------------------------- Tabla Usuarios_2 ☑️
# esquema de la tabla:
# | nombre | apellido | edad | email | nacimiento | adulto | 
# Usaremos una vista de tabla en el panel admin, no hará falta el método str
# para mostrar los campos en admin de usará la clase Usuarios_2Admin (admin.py)

class Usuarios_2(models.Model):
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)
    edad = models.IntegerField()
    email = models.EmailField()
    nacimiento = models.DateField(verbose_name='fecha de nacimiento')   
    adulto = models.BooleanField(verbose_name='mayor de edad')

    def __str__(self):
        return self.nombre
