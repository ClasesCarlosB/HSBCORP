


alumnos = []

while True:
    print("1 - Ver alumnos")
    print("2 - Pedir alumno")
    print("3 - Salir")
    opcion = input("Ingrese opción: ")
    if opcion == "1":
        print("Los alumnos son: ")
        for n in alumnos:
            print(n[0],"-",n[1],"cursos")
    elif opcion == "2":
        nombre = input("Ingrese nombre del alumno: ")
        cursos = input("Ingrese cantidad de cursos: ")
        cursos = int(cursos)
        alumnos.append([nombre,cursos])
        print("Alumnos salvado!")
    elif opcion == "3":
        print("Gracias por usar nuestro programa")
        break
    else:
        print("Error de opción")
    print("")
