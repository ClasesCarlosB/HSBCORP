

productos = []
precios = []

while len(productos) < 5:
    p = input("Ingrese nombre del producto: ")
    c = input("Ingrese precio $: ")
    productos.append(p)
    precios.append(c)
    print("¡Agregado!")
    

print(productos)
print(precios)