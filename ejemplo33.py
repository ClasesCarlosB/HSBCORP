
"""
Armar una calculadora sencilla con Menú

"""


while True:
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Salir")
    opcion = input(">>> ")
    if opcion == "1":
        numero1 = input("Ingrese primer valor: ")
        numero2 = input("Ingrese segundo valor: ")
        try:
            numero1 = float(numero1)
            numero2 = float(numero2)
            r = numero1 + numero2
            print("El resultado es",r)
        except ValueError:
            print("No se puede realizar operación")
    elif opcion == "2":
        numero1 = input("Ingrese primer valor: ")
        numero2 = input("Ingrese segundo valor: ")
        try:
            numero1 = float(numero1)
            numero2 = float(numero2)
            r = numero1 - numero2
            print("El resultado es",r)
        except ValueError:
            print("No se puede realizar operación")
    elif opcion == "3":
        numero1 = input("Ingrese primer valor: ")
        numero2 = input("Ingrese segundo valor: ")
        try:
            numero1 = float(numero1)
            numero2 = float(numero2)
            r = numero1 * numero2
            print("El resultado es",r)
        except ValueError:
            print("No se puede realizar operación")
    elif opcion == "4":
        numero1 = input("Ingrese primer valor: ")
        numero2 = input("Ingrese segundo valor: ")
        try:
            numero1 = float(numero1)
            numero2 = float(numero2)
            r = numero1 / numero2
            print("El resultado es",r)
        except ValueError:
            print("No se puede realizar operación")
        except ZeroDivisionError:
            print("No se puede dividir por cero")
    elif opcion == "5":
        print("Gracias por usar el programa")
        break
    else:
        print("Error de opción")