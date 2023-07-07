

import tkinter as tk


def presionado():
    csaludo.delete(0,tk.END)
    nombre = caja.get()
    frase = "Hola " + nombre
    csaludo.insert(0,frase)



ventana = tk.Tk()
ventana.config(width=300,height=300)
ventana.title("App")

boton = tk.Button(text="Hola!",command=presionado)
boton.place(x=20,y=20)

caja = tk.Entry()
caja.place(x=20,y=120)

etiqueta = tk.Label(text="Ingrese su nombre:")
etiqueta.place(x=20,y=90)


csaludo = tk.Entry()
csaludo.place(x=20,y=200)


ventana.mainloop() 

