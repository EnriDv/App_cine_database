import tkinter as tk
from tkinter.font import BOLD

class Panel:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title('Cinemax')
        self.window.geometry('800x600')
        self.window.config(bg='#fcfcfc')
        self.window.resizable(0,0)

        
