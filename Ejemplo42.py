

import random
import time
import os

"""
Generala
for n in range(5):
    print(random.randint(1,6))
    time.sleep(1)
"""

def azar():
    os.system("cls")
    for n in range(5):
        v = random.randint(0,36)
        print(v)
        time.sleep(0.5)
        os.system("cls")
    return v

def estadistica(valor):
    if valor == 0:
        print("Al piste, salio el cero")
    elif valor <= 12:
        print("Primera docena")
    elif valor <= 24:
        print("Segunda docena")
    else:
        print("Tercer docena")
    
    if valor % 2 == 0:
        print("Par")
    else:
        print("Impar")


os.system("cls")

while True:
    print("1 - Girar ruleta")
    print("2 - Salir")
    opcion = input(">>> ")
    if opcion == "1":
        valor = azar()
        print("Salio el",valor)
        estadistica(valor)
        print("---------------")
    elif opcion == "2":
        print("Gracias por jugar con python casino")
        break
    else:
        print("Error de opción")
    input("Toque ENTER para continuar...")
    os.system("cls")