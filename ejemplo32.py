
while True:
    edad = input("Ingrese su edad: ")
    try:
        edad = int(edad)
        if edad > 0 and edad < 120:
            if edad < 18:
                print("Es menor de edad")
            else:
                print("Es mayor de edad")
        else:
            raise ValueError
        break
    except ValueError:
        print("No se ingreso un numero posible")
        