
import tkinter as tk
#from querry import *


def menu(root):
    menu = tk.Menu(root)

    menu1 = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label='Inicio', menu = menu1)

    menu1.add_command(label='Crear Registro')
    menu1.add_command(label='Eliminar Registro')
    menu1.add_command(label='Salir', command = root.destroy)

    menu.add_cascade(label='Configuracion')
    menu.add_cascade(label='Ayuda')

    lbl_title= tk.Label(root, text="CINEMAX", font =("Bahnschrift SemiBold", 30),
                        bg="#a6192e", fg="white")
    lbl_title.pack(side=tk.TOP, fill=tk.X)
    pass

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()

        self.movie_space()
        self.disable_button()

    def movie_space(self):
        self.label_tittle = tk.Label(self, text= 'Titulo: ')
        self.label_tittle.config(font= ('Arial', 12, 'bold'))
        self.label_tittle.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.entry_tittle = tk.Entry(self)
        self.entry_tittle.config(width = 50)
        self.entry_tittle.grid(row = 0, column = 1, padx = 10, pady = 10)

        self.label_duration = tk.Label(self, text= 'Duracion: ')
        self.label_duration.config(font= ('Arial', 12, 'bold'))
        self.label_duration.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.entry_duration = tk.Entry(self)
        self.entry_duration.config(width = 50)
        self.entry_duration.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        #BOTONES

        self.buton1 = tk.Button(self, text='Boton')
        self.buton1.config(width=20, font= ('Arial', 12, 'bold'),
                           fg = '#dad5d6', bg='#158645',
                           cursor='hand2', activebackground='#35bd6f',
                           command=self.enable_button)
        self.buton1.grid(row=4, column=0, padx = 10, pady = 10)

        self.buton2 = tk.Button(self, text='Boton2')
        self.buton2.config(width=20, font= ('Arial', 12, 'bold'),
                           fg = '#dad5d6', bg='#158645',
                           cursor='hand2', activebackground='#35bd6f',
                           command=self.add_movies)
        self.buton2.grid(row=4, column=1, padx = 10, pady = 10) 

        self.buton3 = tk.Button(self, text='Boton3')
        self.buton3.config(width=20, font= ('Arial', 12, 'bold'),
                           fg = '#dad5d6', bg='#158645',
                           cursor='hand2', activebackground='#35bd6f',
                           command=self.disable_button)
        self.buton3.grid(row=4, column=2, padx = 10, pady = 10) 

    def enable_button(self):
        self.entry_tittle.config(state='normal')
        self.entry_duration.config(state='normal')

        self.buton2.config(state='normal')
        self.buton3.config(state='normal')
        pass

    def disable_button(self):
        self.entry_tittle.config(state='disabled')
        self.entry_duration.config(state='disabled')

        self.buton2.config(state='disabled')
        self.buton3.config(state='disabled')
        pass

    def add_movies(self):
        
        self.disable_button()
        pass

