from tkinter import *
from client.gui import Frame, menu

def main():
    root = Tk()
    root.title("CINE")
    root.resizable(1,1)
    menu(root)

    app = Frame(root = root)

    root.mainloop()

if __name__ == "__main__":
    main()
