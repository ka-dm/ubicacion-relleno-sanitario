import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ttk.Style().configure("TButton", padding=6, relief="flat",
        background="#1978f5")

        # create widgets
        
        # set the controller
        self.controller = None
        
        
        # labe frame parametros
        self.label_frame = ttk.LabelFrame(self, text='Parametros')
        self.label_frame.grid(column=0, row=0, padx=50)
        
        # save button
        self.save_button = ttk.Button(self.label_frame, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=4, column=3, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        # label tamaño area
        self.label_tam_area = ttk.Label(self.label_frame, text='Tamaño del area: ')
        self.label_tam_area.grid(row=0, column=0)

        # tamaño area entry
        self.tam_area_var = tk.StringVar()
        self.tam_area_entry = ttk.Entry(self.label_frame, textvariable=self.tam_area_var, width=10)
        self.tam_area_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # add item button
        self.add_item_button = ttk.Button(self.label_frame, text='+', command=self.add_item_button_clicked)
        self.add_item_button.grid(row=2, column=3, padx=5)
      
        
        # label x
        self.label_tam_area = ttk.Label(self.label_frame, text='x: ')
        self.label_tam_area.grid(row=2, column=0)
        
        # entry x
        self.x_var = tk.StringVar()
        self.x_entry = ttk.Entry(self.label_frame, textvariable=self.x_var, width=10)
        self.x_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # label y
        self.label_tam_area = ttk.Label(self.label_frame, text='y: ')
        self.label_tam_area.grid(row=3, column=0)
        
        # entry y
        self.y_var = tk.StringVar()
        self.y_entry = ttk.Entry(self.label_frame, textvariable=self.y_var, width=10)
        self.y_entry.grid(row=3, column=1, padx=10, pady=5)
        
        # treeview -------------------------------------------------------------
        # define columns
        self.columns = ('1', '2', '3')

        self.tree = ttk.Treeview(self, columns=self.columns, show='headings')
        
        # colums whidth
        self.tree.column('1', width=50, anchor=tk.W)
        self.tree.column('2', width=50, anchor=tk.W)
        self.tree.column('3', width=50, anchor=tk.CENTER)
        
        # define headings
        self.tree.heading('1', text='Ciudad')
        self.tree.heading('2', text='Este')
        self.tree.heading('3', text='Norte')
        
        self.tree.grid(row=0, column=1, sticky='nsew')

        # add a scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=2, sticky='ns')
        # ----------------------------------------------------------------------
        
        # figure matplotlib ----------------------------------------------------
        #self.graficar(10)
        '''# make the data
        n = 10
        m = 10
        
        num = int(self.controller.get_tam_area())
        print("Elvalor es : ", num)
        
        np.random.seed(3)
        x = 4 + np.random.normal(0, 2, 24)
        y = 4 + np.random.normal(0, 2, len(x))
        # size and color:
        sizes = np.random.uniform(15, 80, len(x))
        colors = np.random.uniform(15, 255, len(x))

        # plot
        fig, ax = plt.subplots()
        fig.suptitle('Graficas Ubicaciones')
        
        ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

        ax.set(xlim=(0, n), xticks=np.arange(1, n, step=n/10),
            ylim=(0, n), yticks=np.arange(1, n, step=n/10))
        
        canvas = FigureCanvasTkAgg(fig, master = self)  # Crea el area de dibujo en Tkinter
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=3)'''
        # ----------------------------------------------------------------------

    def set_controller(self, controller):
        self.controller = controller

    def get_tam_area(self):
        return print("cpsa = ", self.controller.get_tam_area())

    def save_button_clicked(self):
        if self.controller:
            self.controller.save()
        
    def add_item_button_clicked(self):
        if self.controller:
            self.controller.add_item(['0',self.x_var.get(), self.y_var.get()], self.tam_area_var.get())
            num = int(self.controller.get_tam_area())
            print(type(num), " ", num)
            self.graficar(num)

    def graficar(self, n):
        # figure matplotlib ----------------------------------------------------
        # make the data
        #n = 10
        #m = 10
        
        np.random.seed(3)
        x = 4 + np.random.normal(0, 2, 24)
        y = 4 + np.random.normal(0, 2, len(x))
        # size and color:
        sizes = np.random.uniform(15, 80, len(x))
        colors = np.random.uniform(15, 255, len(x))

        # plot
        fig, ax = plt.subplots()
        fig.suptitle('Graficas Ubicaciones')
        
        ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

        ax.set(xlim=(0, n), xticks=np.arange(1, n, step=n/10),
            ylim=(0, n), yticks=np.arange(1, n, step=n/10))
        
        canvas = FigureCanvasTkAgg(fig, master = self)  # Crea el area de dibujo en Tkinter
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=3)