""" ------------------------------------------------ App_Formulario => admin """
"""
Registro de las tablas en el panel de administración y clases para presentación
de los campos

Clases para presentación de campos
- FormularioAdmin
- Formulario_2Admin

Tablas registradas en panel administrativo:
- Formulario
- Formulario_2
"""

from django.contrib import admin
from App_Formulario.models import Formulario, Formulario_2

# Register your models here.


# ---------------------------------------- Clases para presentación de campos ☑️

# ------------------------------------------------------------- Tabla Formulario
class FormularioAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_usuario', 
        'nombre',
        'apellido', 
        'email',
        'edad',
        'peso',
        'altura',
        'fecha_nacimiento',
        'ultimo_login',
        'esta_activa',
        'es_personal',
        'roles')

    search_fields = (
        'nombre_usuario', 
        'nombre',
        'apellido', 
        'email',
        'edad',
        'peso',
        'altura',
        'fecha_nacimiento',
        'ultimo_login',
        'esta_activa',
        'es_personal',
        'roles')



# ----------------------------------------------------------- Tabla Formulario_2
class Formulario_2Admin(admin.ModelAdmin):
    list_display = [
            'usuario',
            'foto',
            'password_1',
            'password_2',
            'suscrito'
        ]

    search_fields = [
            'usuario',
            'foto',
            'password_1',
            'password_2',
            'suscrito'
        ]



# ----------------------------- Tablas registradas en el panel administrativo ☑️


# ------------------------------------------------------------- Tabla Formulario
admin.site.register(Formulario, FormularioAdmin)


# ----------------------------------------------------------- Tabla Formulario_2
admin.site.register(Formulario_2, Formulario_2Admin)

