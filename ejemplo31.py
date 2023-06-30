"""

Tarea:
Escribe un programa que guarde en una lista, los números pares en un rango dado,
por teclado, teniendo en cuenta que queremos el último inclusive.

"""


li = input("Ingrese limite inferior: ")
li = int(li)

ls = input("Ingrese limite superior: ")
ls = int(ls)


if li < ls:
    pares = []

    for n in range(li,ls+1,1):
        if n % 2 == 0:
            pares.append(n)
        
    print(pares)
else:
    print("El limite inferior no puede ser mayor o igual \n que el limite superior!")
    
    
