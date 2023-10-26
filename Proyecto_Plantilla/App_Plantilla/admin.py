""" ------------------------------------------------- App Plantilla => admin """
"""
Registro de las tablas en el panel de administración y clases para presentación
de los campos

Clases para presentación de campos
- Usuarios_2Admin => 1-campos a mostrar | 2-campos a emplear en búsquedas

Tablas registradas en panel administrativo:
- Usuarios
- Usuarios_2
"""

from django.contrib import admin
from App_Plantilla.models import Usuarios, Usuarios_2   # importación del modelo desde APP/models.py

# Register your models here.

# ---------------------------------------- Clases para presentación de campos ☑️

class Usuarios_2Admin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'email', 'nacimiento', 'adulto')   # 1
    search_fields = ('nombre', 'apellido', 'email')                                  # 2



# -------------------------------- Tablas registradas en panel administrativo ☑️

# --------------------------------------------------------------- Tabla Usuarios
admin.site.register(Usuarios)   



# ------------------------------------------------------------- Tabla Usuarios 2
admin.site.register(Usuarios_2, Usuarios_2Admin) 