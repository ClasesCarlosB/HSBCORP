

import tkinter as tk
import random
import sys

def estadistica(valor):
    mensaje_uno = ""
    mensaje_dos = ""
    if valor == 0:
        mensaje_uno = "Al piste, salio el cero"
    elif valor <= 12:
        mensaje_uno = "Primera docena"
    elif valor <= 24:
        mensaje_uno = "Segunda docena"
    else:
        mensaje_uno = "Tercer docena"
    

    if valor % 2 == 0:
        mensaje_dos = "Par"
    else:
        mensaje_dos = "Impar"
    
    return [mensaje_uno,mensaje_dos]


def presionado():
    cresultado.delete(0,tk.END)
    cdocena.delete(0,tk.END)
    cpar.delete(0,tk.END)
    valor = random.randint(0,36)
    cresultado.insert(0,valor)
    r = estadistica(valor)
    cdocena.insert(0,r[0])
    cpar.insert(0,r[1])
    

def salir():
    sys.exit()
    


###################################3

ventana = tk.Tk()
ventana.config(width=250,height=300)
ventana.title("Casino 2.0")
bjugar = tk.Button(text="Jugar",command=presionado)
bjugar.place(x=20,y=20,width = 80,height = 40)

bsalir = tk.Button(text="Salir",command=salir)
bsalir.place(x=140,y=20,width = 80,height = 40)

eresultado = tk.Label()
eresultado.place(x=60,y=70)

cresultado = tk.Entry()
cresultado.place(x=60,y=100)


edocena = tk.Label()
edocena.place(x=60,y=150)

cdocena = tk.Entry()
cdocena.place(x=60,y=180)


epar = tk.Label()
epar.place(x=60,y=230)
cpar= tk.Entry()
cpar.place(x=60,y=260)


ventana.mainloop()


