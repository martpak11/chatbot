from random import randint

def answer(eleccion):
    if eleccion == '1':
       info = print('El colegio se enfoca principalmente en el desalloro de los alumnos, su manera de comunicarse en ocasiones formales y en el ingles bien pronunciado.')
       return info
    elif eleccion == '2':
        days = input('Los horarios son de Lunes a Viernes de 7.45hs hasta las 16.30hs y el almuerzo de 12.50hs hasta 13.30hs, los estudiantes pueden elegir si comer comedor, bianda, salir a comprar o ir a su casa para comer.¿Quieres saber los precios del comedor?')
        if days == 'si':
            print('Los precios aumentan cada dos meses pero actualmente esta en $15.000.')
    elif eleccion == '3':
        descuentos = input('''
El colegio tiene un valor total de 500k por mes.
¿Quieres ver algunos descuentos?
''')
        if descuentos == 'si':
            descuentos = print('Para alumnos nuevos hay un descuento de un 10% y para alumnos con hermanos hay un descuento del 15%.')
            return descuentos
    elif eleccion == '4':
        print('La institución cuenta con una actividad extrecurricular donde se hace un sorteo para recolectar plata y poder donarla.')
        donation = input('¿Quieres comprar una rifa?')
        if donation == 'si':
            number = print('Tu número es:', randint(0,100))
            winner = print('Número ganador:', randint(0,100))
            return 
    elif eleccion == '5':
        professors = print('Los profesores varian según la materia, cada asignatura tiene un docente distinto.')
        return professors
    elif eleccion == '6':
        asignature = print('En la institución se aprueba con 6 y si un estudiante no aprobó alguna materia, tiene los periodos de Diciembre, Febrero y Previas para poder levantar su nota.')
        asignature = input('¿Quieres saber más sobre los periodos de recuperación?')
        if asignature == 'si':
            asignature = print('En los periodos de diciembre y febrero cada estudiante cuenta con dos oportunidades para recuperar y, en caso de haber fallado en estas oportunidades, las materias quedan como previas y tienen varias pruebas a lo largo del año para aprobar.')
            return asignature
    else:
        return 'Lo siento, no te entendí.'