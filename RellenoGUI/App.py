import tkinter as tk
from tkinter import messagebox
from Controller import Controller
from Model import Model
from View import View

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Localizacion de relleno sanitario')
        model = Model()
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)
        controller = Controller(model, view)
        view.set_controller(controller)

def on_closing():
    if messagebox.askokcancel("Salir", "¿Quieres salir?"):
        app.destroy()
        
if __name__ == '__main__':
    app = App()
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()