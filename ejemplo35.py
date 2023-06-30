comentario = "La verdad que el servicio de catering fue bueno, la musica y el ambiente fue bueno"
c = comentario.split()
print(c)


frecuencias = {}

for n in c:
    a = n.lower()
    if a not in frecuencias:
        frecuencias[a] = 1
    else:
        frecuencias[a] +=1

print("----------------")
print("\n"*3)
print("----------------")

print(frecuencias)

