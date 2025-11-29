from analizador import *
eleccion = input('''
Hola! ¿Que necesitas?
    1) Colegio
    2) Horarios
    3) Precio
    4) Actividades extracurriculares
    5) Profesores
    6) Formas de aprobar
    7) Si desea salir''')

while eleccion != '7':
    answer(eleccion)
    eleccion = input('''
    1) Colegio
    2) Horarios
    3) Precio
    4) Actividades extracurriculares
    5) Profesores
    6) Formas de aprobar
    7) Si desea salir''')