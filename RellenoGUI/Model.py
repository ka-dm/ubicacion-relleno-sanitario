import tkinter
from tkinter.constants import BOTH

raiz = tkinter.Tk()
raiz.title("Primera Interfaz")
raiz.config(bg="red")

miFrame = tkinter.Frame(raiz)
#miFrame.pack(expand=True, fill="both")
miFrame.pack()
miFrame.config(bg="blue")
miFrame.config(width="500", height="500")


raiz.mainloop()