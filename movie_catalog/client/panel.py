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

    def select_genre(self):
        con = Conect()
        con.cursor.execute("""SELECT DISTINCT GENRE FROM MOVIE""")
        row = con.cursor.fetchall()
        con.exit()
        self.var=tk.StringVar(self.window)
        self.var.set('None')
        opciones = row
        self.option = tk.OptionMenu(self.window, self.var, *opciones).place(x=220, y =120)
        self.option.pack(side='left', padx=10, pady=10)
    
        