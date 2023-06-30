"""
String ----> si los str

Recorrer
Metodos

"""

print("Concatenar +")

frase = "Hoy"+" "+ "es viernes "
print(frase)

print("---------------------------------------")
print("---------------------------------------")
    

texto = "Hola Mundo!"

#recorrer
print("Recorrer")
for n in texto:
    print(n)
    
print("---------------------------------------")
print("---------------------------------------")
    
# indice
print("Indice")
print("Pos 0:",texto[0])
print("Pos 6:",texto[6])

print("---------------------------------------")
print("---------------------------------------")
    
print("Poner Mayusculas:")
a = texto.upper()
print(a)

print("Poner en Minuscula")
b = texto.lower()
print(b)


print("---------------------------------------")
print("---------------------------------------")
    
print("Empieza con Hola?")
print(texto.startswith("Hola"))

print("Termina con Mundo!")
print(texto.endswith("Mundo!"))

print("Termina con !")
print(texto.endswith("!"))

print("Termina con curso:")
print(texto.endswith("curso"))


print("---------------------------------------")
print("---------------------------------------")

print("Esta Mundo?")
print(texto.find("Mundo"))
print("Futbol")
print(texto.find("Futbol"))

print("---------------------------------------")
print("---------------------------------------")

frase = "Uno busca lleno de esperanzas.... Uno .... Uno"

print(frase)
print("¿Cuantas veces se repite Uno?")
print(frase.count("Uno"))

print("---------------------------------------")
print("---------------------------------------")

cita = "Tenia un gato que se llamaba indiana"
print(cita)
cita = cita.replace("gato","perro")
print(cita)



print("---------------------------------------")
print("---------------------------------------")


print("Strip")

nombre = " Juan "
print(nombre)
print(nombre.strip())


print("---------------------------------------")
print("---------------------------------------")


print("Strip")

nombre = "       Juan    "
print(nombre)
print(nombre.strip())


print("Carecteres especiales")
print("Renglon1 \n\tRenglon2")



print("---------------------------------------")
print("---------------------------------------")

comentario = "La verdad que el servicio de catering fue bueno, la musica y el ambiente fue bueno"
c = comentario.split() 
print(c)


print("---------------------------------------")
print("---------------------------------------")


"""
str.isdecimal(): sirve para saber si hay numeros en un texto solo numeros
str.swapcase(): cambiar may por min e inversa
str.title(): Poner la primer letra de cada palabra en mayus
str.capitalize: Solo pone mayuscula la primer letra de un texto

"""