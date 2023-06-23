


"""

break y continue

break termina el bucle.

continue pasa desde donde este, a la siguiente vuelta.



"""





while True:
    print("1 - Saludar")
    print("2 - Pedir nombre")
    print("3 - Salir")
    opcion = input("Ingrese opción: ")
    if opcion == "1":
        print("HOLA!")
    elif opcion == "2":
        nombre = input("Ingrese su nombre: ")
        print("Recibido", nombre)
    elif opcion == "3":
        print("Gracias por usar nuestro programa")
        break
    else:
        print("Error de opción")
    print("")
    print("Final del bucle")
    print("")
        







