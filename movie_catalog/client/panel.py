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
        self.var=tk.StringVar(self.window)
        self.var.set('None')

        label=tk.Label(self.window, text="Select Genre:", font =("goudy old style", 18), bg="#fcfcfc").place(x=50, y =118)
        boton = tk.Button(text='Obtain', command=self.select_genre).place(x=350,y=123)
        self.window.mainloop()
        
        

    def select_genre(self):
        con = Conect()
        con.cursor.execute("""SELECT DISTINCT GENRE FROM MOVIE""")
        op = con.cursor.fetchall()
        con.exit()
        opera = []
        for n in op:
            opera.append(n[0])
        opciones = opera
        print(self.var.get())
        self.option = tk.OptionMenu(self.window, self.var, *opciones).place(x=220, y =120)
        if self.var.get() == 'None':
            pass
        else:
            self.create_table(str(self.var.get()))
        

    def create_table(self,gen):
        con=Conect()
        con.cursor.execute("""SELECT TITLE, DURATION_, CLASIFICATION FROM MOVIE WHERE GENRE = :gen""", {'gen': gen})
        datos = con.cursor.fetchall()

        window = tk.Tk()
        window.title("Tabla")

        table = ttk.Treeview(window)
        table["columns"] = ("Title", "Duration", "Clasification")

        table.column("#0", width=0, stretch=tk.NO)  
        table.column("Title", anchor=tk.W, width=100)
        table.column("Duration", anchor=tk.W, width=80)
        table.column("Clasification", anchor=tk.W, width=100)

        table.heading("#0", text="", anchor=tk.W)
        table.heading("Title", text="Title", anchor=tk.W)
        table.heading("Duration", text="Duration", anchor=tk.W)
        table.heading("Clasification", text="Clasification", anchor=tk.W)

        for dato in datos:
            table.insert("", tk.END, values=dato)
        table.pack()
       
        
        
