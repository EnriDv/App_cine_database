from tkinter import messagebox
from conexion import *

class Query:
    def __init__(self):
        pass

    def consult_movies(self):
        try:
            con = Conect()
        except Exception as e:
            messagebox('Error',('Nose pudo conectar a la base de datos: '+str(e)))

        try:
            con.cursor.execute(""" select * from MOVIE""")
        except Exception as e:
            messagebox('Error',('Nose pudo realizar la consulta: '+str(e)))
            
            