
"""

[[nombre,cursos].....]

{"juan":5,"roberto":10,"susana":2}

"""

alumnos = {}

while True:
    print("1 - Ver alumnos")
    print("2 - Pedir alumno")
    print("3 - Ver un alumno puntual")
    print("4 - Salir")
    opcion = input("Ingrese opción: ")
    if opcion == "1":
        print("Los alumnos son: ")
        for n in alumnos:
            print(n,"-",alumnos[n],"cursos")
    elif opcion == "2":
        nombre = input("Ingrese nombre del alumno: ")
        cursos = input("Ingrese cantidad de cursos: ")
        cursos = int(cursos)
        alumnos[nombre] = cursos
        print("Alumnos salvado!")
    elif opcion == "3":
        nombre = input("Ingrese alumno para verificar: ")
        if nombre in alumnos:
            print(nombre,"tiene",alumnos[nombre],"cursos asignados")
        else:
            print(nombre,"no está en alumnos")
    elif opcion == "4":
        print("Gracias por usar nuestro programa")
        break
    else:
        print("Error de opción")
    print("")

