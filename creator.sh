#! /bin/zsh

# CREADOR DE ENTORNOS DJANGO
#Ubicar el script en la carpeta repositorio del proyecto



# project
function project(){
    # Crea el proyecto solicitando el nombre del mismo
    echo "Nombre del Proyecto: ${yellow}[ usar prefijo Proyecto_ ]${blanco}"
    read nombre_project
    django-admin startproject ${nombre_project}
    echo "Creado el proyecto ${turquoise}${nombre_project}  ${blanco}"
}




# ----------------------------------------------------------- Colores para texto
blanco="\033[0m\e[0m"
green="\e[0;32m\033[1m"
red="\e[0;31m\033[1m"
blue="\e[0;34m\033[1m"
yellow="\e[0;33m\033[1m"
turquoise="\e[0;36m\033[1m"
purple="\e[0;35m\033[1m"
grey="\e[0;30m\033[1m"



# ------------------------------------- instrucciones para el Gestor de Proyecto
# Diccionario contenedor de instrucciones para el gestor
# dict[instruccion]=tarea

declare -A dict
dict[proyecto]=project
dict[env]=enviroment
dict[desactivar]="deactivate"



# --------------------------------------------------------- Ejecución del Script
# Presentación del Creador al usuario y solicitud de la instrucción

echo -e ${purple} GUScode ${blanco} Creador de proyectos Django 
echo -e Ingrese ${red}lista${blanco} para ver las opciones
echo -e Instrucción ${purple}󰒊${blanco}  
read tarea


if [[ ${dict[$tarea]} ]]; then
    echo "Ejecutando =>\n"
    eval ${dict[$tarea]}
else
    echo "La instrucción no es correcta"
fi