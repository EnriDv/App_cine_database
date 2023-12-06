from tkinter import *
import conexion

def mensaje():
    print("boton")

ventana = Tk()
ventana.geometry("800x480")
ventana.title("CATALOGO")

lbl = Label(ventana, text='CATALOGO DE PELICULAS')
lbl.pack()

btn = Button(ventana, text='Presionar para\nrealizar una conulta', command=conexion.consult)
btn.pack()

ventana.mainloop()