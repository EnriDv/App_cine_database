
import tkinter as tk

def menu(root):
    menu = tk.Menu(root)
    root.config(menu = menu, width=300, height =300)

    menu1 = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label='Inicio', menu = menu1)

    menu1.add_command(label='Crear Registro')
    menu1.add_command(label='Eliminar Registro')
    menu1.add_command(label='Salir', command = root.destroy)

    menu.add_cascade(label='Configuracion')
    menu.add_cascade(label='Ayuda')

    pass

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width=480, height=320)
        self.root = root
        self.pack()
        #self.config( bg='white')
        self.movie_space()

    def movie_space(self):
        self.label_tittle = tk.Label(self, text= 'Titulo: ')
        self.label_tittle.config(font= ('Arial', 12, 'bold'))
        self.label_tittle.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.entry_tittle = tk.Entry(self)
        self.entry_tittle.config(width = 50, state = 'disable')
        self.entry_tittle.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.label_duration = tk.Label(self, text= 'Duracion: ')
        self.label_duration.config(font= ('Arial', 12, 'bold'))
        self.label_duration.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.entry_duration = tk.Entry(self)
        self.entry_duration.config(width = 50, state = 'disable')
        self.entry_duration.grid(row = 1, column = 1, padx = 10, pady = 10)
        

        #BOTONES

        self.buton1 = tk.Button(self, text='Boton')
        self.buton1.config(width=20, font= ('Arial', 12, 'bold'),
                           fg = '#dad5d6', bg='#158645',
                           cursor='hand2', activebackground='#35bd6f')
        
        self.buton1.grid(row=4, column=0)

        pass
        











"""
import conexion

def mensaje():
    print("boton")

ventana = Tk()
ventana.geometry("800x480")
ventana.title("CATALOGO")

lbl = Label(ventana, text='CATALOGO DE PELICULAS')
lbl.pack()

btn = Button(ventana, text='Presionar para\nrealizar una conulta', command= conexion.query)
btn.pack()

btn2 = Button(ventana, text='Presionar para salir', command= conexion.exit)
btn2.pack()

ventana.mainloop()
"""