
"""
Un empleado cobró 300 dólares por mes desde enero
a junio, 500 dólares de julio a octubre, y 700 dólares
por mes en noviembre y en diciembre.

Hace un programa que calcule el sueldo promedio. Y
que diga si este “empleado” está cobrando un sueldo
bajo, normal o mejor de lo normal.
● Sueldo bajo: por debajo de 300 dólares.(no inclusive)
● Sueldo normal: entre 300 a 900. (300 inclu, y 900 sin incluir)
● Sueldo mejor de lo normal: más de 900 dólares.(900 incluido)


"""

total = (300 * 6) + (500 * 4) + (700 * 2)

promedio = total / 12

print("El sueldo promedio es:",promedio)

"""
if promedio < 300:
    print("Sueldo bajo")
elif promedio < 900:
    print("Sueldo normal")
else:
    print("Sueldo mejor de lo normal")
"""

"""
if promedio < 300:
    print("Sueldo bajo")
else:
    if promedio < 900:
        print("Sueldo normal")
    else:
        print("Sueldo mejor de lo normal")

"""

if promedio < 300:
    print("Sueldo bajo")
    
if promedio >= 300 and promedio < 900:
    print("Sueldo normal")
    
if promedio >= 900:
    print("Sueldo mejor de lo normal")