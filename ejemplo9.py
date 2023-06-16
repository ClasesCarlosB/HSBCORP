
"""
Se preguntará el tipo de rol que desempeña una
persona en una institución por una entrada del
tipo input. Los valores posibles son “admin” o
“profesor”.
Luego si la persona es “admin” o “profesor”, se
debería pedir la contraseña, siendo la única válida
“1234” (la contraseña se toma como string). Si
la contraseña ingresada es válida, se procederá a
pedir el nombre de la persona, y si no es vacío, se
lo saludará.
Contemplar los casos donde no se cumple como
corresponde y mostrar un mensaje en pantalla
"""

rol = input("Ingrese rol: ")

if rol == "admin" or rol == "profesor":
    clave = input("Ingrese clave: ")
    if clave == "1234":
        nombre = input("Ingrese su nombre: ")
        if nombre != "":
            print("Bienvenid@",nombre)
        else:
            print("Bienvenido anonimo")
    else:
        print("Clave incorrecta")
else:
    print("Error de rol")
        
