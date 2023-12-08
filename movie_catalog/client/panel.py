import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
from client.conexion import Conect

class Panel:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title('Cinemax')
        self.window.geometry('800x600')
        self.window.config(bg='#fcfcfc')
        self.window.resizable(0,0)
        
        self.lbl_title= tk.Label(self.window, text="CINEMAX", font =("Bahnschrift SemiBold", 30),
                        bg="#a6192e", fg="white")
        self.lbl_title.pack(side=tk.TOP, fill=tk.X)

        label=tk.Label(self.window, text="Select Genre:", font =("goudy old style", 18), bg="#fcfcfc").place(x=50, y =118)
        self.select_genre()
        boton = tk.Button(text='Obtain').place(x=350,y=123)
        self.window.mainloop()
        
        

    def select_genre(self):
        con = Conect()
        con.cursor.execute("""SELECT DISTINCT GENRE FROM MOVIE""")
        op = con.cursor.fetchall()
        con.exit()
        self.var=tk.StringVar(self.window)
        self.var.set('None')
        opciones = op
        print(self.var.get())
        self.option = tk.OptionMenu(self.window, self.var, *opciones).place(x=220, y =120)
        

    def crear_tabla(self,gen):
        con=Conect()
        con.cursor.execute("""SELECT TITLE, DURATION_, CLASIFICATION FROM MOVIE WHERE GENRE = :gen""", {'gen': gen})
        datos = con.cursor.fetchall()

        # Crear ventana
        ventana = tk.Tk()
        ventana.title("Tabla")

        # Crear tabla
        tabla = ttk.Treeview(ventana)

        # Definir columnas
        tabla["Genre"] = ("Title", "Duration", "Clasification")

        # Configurar encabezados de columna
        tabla.column("#0", width=0, stretch=tk.NO)  # Columna oculta
        tabla.column("Title", anchor=tk.W, width=100)
        tabla.column("Duration", anchor=tk.W, width=50)
        tabla.column("Clasification", anchor=tk.W, width=100)

        # Configurar encabezado
        tabla.heading("#0", text="", anchor=tk.W)
        tabla.heading("Title", text="Title", anchor=tk.W)
        tabla.heading("Duration", text="Duration", anchor=tk.W)
        tabla.heading("Clasification", text="Clasification", anchor=tk.W)

        for dato in datos:
            tabla.insert("", tk.END, values=dato)
        tabla.pack()
        ventana.mainloop()
        
        