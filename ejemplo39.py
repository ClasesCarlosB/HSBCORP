"""
Un estudio inmobiliario decide construir
un sistema de calculo de area, para
dar la superficie total de un inmueble
"""


def calcular(b,a):
    sup = b * a
    return sup


total = 0

while True:
    print("1 - Agregar ambiente")
    print("2 - Calcular y terminar")
    opcion = input(">>> ")
    if opcion == "1":
        base = input("Ingrese base metros: ")
        base = float(base)
        ancho = input("Ingrese ancho metros: ")
        ancho = float(ancho)
        parcial = calcular(base,ancho)
        total = total + parcial
    elif opcion == "2":
        print("El total de m2 es:",total)
        print("Gracias por usar el programa")
        break
    else:
        print("Error de opción")
    print("")
        