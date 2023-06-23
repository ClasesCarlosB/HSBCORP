

almacen = []

#almacen <-- ["fideos",120]
#        <-- ["galletitas",500]

# almacen.append(["fideos",120]) 
# [p , c]

contador = 0

while contador < 5:
    p = input("Ingrese nombre del producto: ")
    c = input("Ingrese precio del producto: ")
    c = float(c)
    almacen.append([p,c])
    print("Producto agregado!")
    contador = contador + 1

#print(almacen)

print("La lista de precios: ")
for n in almacen:
    print(n[0],"- $",n[1])