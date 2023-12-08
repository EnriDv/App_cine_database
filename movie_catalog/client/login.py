from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from client.panel import Panel
from client.conexion import Conect

class App:
    def verify(self):
        con = Conect()
        try:
            con.cursor.execute(""" select USERNAME, PASSWORD_ from ACCOUNT""")
            row = con.cursor.fetchall()
        except:
            print('ERROR')
            
        user = self.usuario.get()
        password = self.password.get()
        if (user, password) in row:
            self.window.destroy()
            con.exit()
            Panel()
        else:
            messagebox.showerror(message="Ususario o Contraseña incorrecta", title='Error')
        

    def __init__(self):
        
        self.window = Tk()
        self.window.title('Login')
        self.window.geometry('400x600')
        self.window.config(bg='#fcfcfc')
        self.window.resizable(0,0)

        #FRAME
        frame = Frame(self.window, bd=0, relief=SOLID, bg='#fcfcfc')
        frame.pack(side='right', expand=YES, fill=BOTH)
        
        #FRAME TOP
        frame_top =Frame(frame, height=50, bd=0, relief=SOLID, bg='black')
        frame_top.pack(side='top', fill=X)
        tittle = Label(frame_top, text='Login', font=('Times', 30), fg='#666a88', bg='#fcfcfc', pady=50)
        tittle.pack(expand=YES, fill=BOTH)

        #FRAME FILL
        frame_fill = Frame(frame, height=50, bd=0, relief=SOLID, bg='#fcfcfc')
        frame_fill.pack(side='bottom', expand=YES, fill=BOTH)

        label_usser = Label(frame_fill, text='Usser', font=('Times', 14), fg='#666a88', bg='#fcfcfc', anchor='w')
        label_usser.pack(fill=X, padx=20, pady=5)
        self.usuario = Entry(frame_fill, font=('Times', 14))
        self.usuario.pack(fill=X, padx=20, pady=10)

        label_password = Label(frame_fill, text='Password', font=('Times', 14), fg='#666a88', bg='#fcfcfc', anchor='w')
        label_password.pack(fill=X, padx=20, pady=5)
        self.password = Entry(frame_fill, font=('Times', 14))
        self.password.pack(fill=X, padx=20, pady=10)
        self.password.config(show='*')

        button = Button(frame_fill, text='Login', font=('Times',15, BOLD), bg='#3a7f66', bd=0, fg='#fff', command=self.verify)
        button.pack(fill=X, padx=20, pady=20)

        self.window.mainloop()
