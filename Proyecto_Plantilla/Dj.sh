#! /bin/zsh

# GESTOR DE PROYECTOS DJANGO
# Ubicar archivo en la carpeta de Proyecto General (core)



# -------------------------------------------------------------------- Funciones
# funciones para manage.py que soliciten parámetros

# project
function project(){
    # Crea el proyecto solicitando el nombre del mismo
    echo "Nombre del Proyecto: ${yellow}[ usar prefijo Proyecto_ ]${blanco}"
    read nombre_project
    django-admin startproject ${nombre_project}
    echo "Creado el proyecto ${turquoise}${nombre_project}  ${blanco}"
}


# app
function app(){
    # Crea aplicaciones solicitando el nombre
    echo "Nombre de nueva Aplicación: ${yellow}[ usar el prefijo App_ ]${blanco}"
    read nombre_app
    python manage.py startapp ${nombre_app}
    echo "Creada la aplicación ${turquoise}${nombre_app}  ${blanco}"
}


# git
function git_upgrade(){
    # Actualiza repositorio GitHub del proyecto
    echo "Mensaje de commit:"
    read mensaje
    eval $(ssh-agent -s); 
    ssh-add ~/id_rsa; 
    git add .
    git commit -m "${mensaje}"
    git push
    echo "${turquoise}Repositorio Actualizado   ${blanco}"
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
dict[run]="python manage.py runserver"
dict[proyecto]=project
dict[migraciones]="python manage.py makemigrations"
dict[migrar]="python manage.py migrate"
dict[aplicacion]=app
dict[git]=git_upgrade


# --------------------------------------------------------- Ejecución del Script
# Presentación del Gestor al usuario y solicitud de la instrucción

echo -e ${turquoise} GUScode ${blanco} Gestor de proyectos Django 
echo -e Instrucción ${turquoise}󰒊${blanco}  
read tarea


if [[ ${dict[$tarea]} ]]; then
    echo "Ejecutando =>\n"
    eval ${dict[$tarea]}
else
    echo "La instrucción no es correcta"
fi