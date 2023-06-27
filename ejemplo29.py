"""


Sentencias de control
if
while
for


Colecciones

Listas
    Se crean con [items,...] y se acceden con [indice]
    Son mutables, cambian
    Tienen met
        .append() # agrega al final
        .insert() # agrega donde yo quiero
        existen otros, pero estos 2 son muy importantes


Tuplas
    Se crean con (items,) y se accede con [indice]
    Son inmutables
    No tienen met
    

Diccionarios
    Se crean con {claves:valores}, y se accede con [clave]    
    clave ---> valor
    
    
    

len()
del 

Operador de Pertenencia
in
not in


"""


jugadores = {"messi": 10, "diamria": 11, "martinez": 23}

for n in jugadores:
    print(n, "-", jugadores[n])


print("\n"*3)


productos = {"fideos": 200, "arroz": 400, "manteca": 350, "gaseosa": 600}

for n in productos:
    print(n, "- $", productos[n])


