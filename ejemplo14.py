
"""
Listas

Ejemplo
nombre = [10,2,70]

Se crean con un nombre igual
que las variables("plural"),
y el contenido estara dado por
[] y dentro cada item separado
por coma 
Para acceder vamos a usar nombre[indice] ---> 
retorna el valor
de ese item en esa posición.

¿Qué pasa si quiero cambiar los valores?
No pasa nada, se puede


nombre[indice] = nuevo_valor


Un nuevo problema....

Es que cuando vos tenes que agregar un item... ¿Como lo haces?
Borras todo? Volves armar todo? 
No

Metodos de las listas
    -append(item) agrega al final
    -insert(item) agrega en una determinada posición
 

"""

vacia = []

persona = ["Juan",30,3,True]

numeros = [10,20,30]

print("Todos los",
      numeros[0],
      "de cada mes me dan",
      numeros[1],
      "dolares para ahorrar y los", 
      numeros[2],
      "verifico mis ahorros")


print(persona)

persona[2] = 10
persona[3] = False

persona[1] = persona[1] + 1

print(persona)

#agrego al final
persona.append(2050.3)

print(persona)

#insert agrega un item en una posición
persona.insert(1,"Rodriguez")

print(persona)

cantidad = len(persona)

print(cantidad)

#elimino el item en la pos 2, se va la edad
del persona[2]

print(persona) 
