

"""

Pedir por teclado 2 numeros,
el primero limite inf, y el segundo el limite sup
inclusive.

Luego el programa debe mostrar los numeros que son 
multiplos de 3 y de 5 en ese rango.



"""

limite_inf = input("Ingrese lim inf: ")
limite_inf = int(limite_inf)

limite_sup = input("Ingrese lim sup: ")
limite_sup = int(limite_sup)


contador = limite_inf

while contador <= limite_sup:
    if contador % 3 == 0 and contador % 5 == 0:
        print("El numero:",contador,"cumple")
    contador = contador + 1
