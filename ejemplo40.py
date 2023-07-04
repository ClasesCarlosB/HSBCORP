


def input_enteros(frase):
    x = input(frase)
    while True:
        try:
            x = int(x)
            break
        except ValueError:
            print("Error. Solo enteros")
        x = input("Nuevamente. "+frase)
    return x


#####################


edad = input_enteros("Ingrese su edad: ")
hijos = input_enteros("Cantidad de hijos: ")

print(edad,type(edad))
print(hijos,type(hijos))
