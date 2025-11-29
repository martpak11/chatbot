from random import randint
def answer(eleccion):
    if eleccion == '1':
       info = print(' colegio se enfoca principalmente en el desalloro de los alumnos, su manera de comunicarse en ocasiones formales y en el ingles')
       return info
    elif eleccion == '2':
        days = print('Los horarios son de Lunes a Viernes de 7.45hs hasta las 16.30hs y un almuerzo de 12.50hs hasta 13.30hs')
    elif eleccion == '3':
        descuentos = input('''
El colegio tiene un valor total de 500k por mes
¿Quieres ver algunos descuentos?
''')
        if descuentos == 'si':
            descuentos = print('Para alumnos nuevos hay un descuento de un 10% y para alumnos con hermanos hay un descuento del 15%')
            return descuentos
    elif eleccion == '4':
        print('La institución cuenta con una actividad extrecurricular donde se hace un sorteo para recolectar y poder donarla')
        donation = input('¿Quieres comprar una rifa?')
        if donation == 'si':
            number = print('Tu número es:', randint(0,100))
            print('NNúmero ganador:', randint(0,100))
            return number
    elif eleccion == '5':
        professors = print('Los profesores varian segun la materia, cada asignatura tiene un docente distinto')
        return professors
    elif eleccion == '6':
        asignature = print('En la institución se aprueba con 6 y si un estudiante no aprobo alguna materia, tiene los periodos de Diciembre, Febrero y Previas para poder levantar su nota')
        return asignature
    elif eleccion == '7':
        return
    else:
        return 'Lo siento, no te entendi'