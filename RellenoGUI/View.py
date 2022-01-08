import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(self, text='Email:')
        self.label.grid(row=3, column=3)

        # email entry
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=3, column=4, sticky=tk.NSEW)

        # save button
        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=3, column=5, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        # set the controller
        self.controller = None
        
        
        self.label_frame = ttk.LabelFrame(self, text='Parametros')
        self.label_frame.grid(column=0, row=0, padx=50, pady=50)
        
        # label tamaño area
        self.label_tam_area = ttk.Label(self.label_frame, text='Tamaño del area: ')
        self.label_tam_area.grid(row=0, column=0)

        # tamaño area entry
        self.tam_area_var = tk.StringVar()
        self.tam_area_entry = ttk.Entry(self.label_frame, textvariable=self.tam_area_var, width=10)
        self.tam_area_entry.grid(row=0, column=1, sticky=tk.NSEW)
        
        # add item button
        self.add_item_button = ttk.Button(self.label_frame, text='Agregar punto', command=self.add_item_button_clicked)
        self.add_item_button.grid(row=4, column=0, padx=10)
        
        # label x
        self.label_tam_area = ttk.Label(self.label_frame, text='x: ')
        self.label_tam_area.grid(row=2, column=0)
        
        # entry x
        self.x_var = tk.StringVar()
        self.x_entry = ttk.Entry(self.label_frame, textvariable=self.x_var, width=10)
        self.x_entry.grid(row=2, column=1, sticky=tk.NSEW)
        
        # label y
        self.label_tam_area = ttk.Label(self.label_frame, text='y: ')
        self.label_tam_area.grid(row=3, column=0)
        
        # entry y
        self.y_var = tk.StringVar()
        self.y_entry = ttk.Entry(self.label_frame, textvariable=self.y_var, width=10)
        self.y_entry.grid(row=3, column=1, sticky=tk.NSEW)
        
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
        nombres = ['Azul', 'Rojo', 'Verde', 'Magenta','Negro']
        colores = ['blue','red','green','magenta', 'black']
        tamaño = [15, 25, 10, 20, 30]

        fig, axs = plt.subplots(dpi=80, figsize=(5, 5), sharey=True, facecolor='#00f9f844')
        fig.suptitle('Graficas Matplotlib')

        axs.scatter(nombres, tamaño, color = colores)
        
        canvas = FigureCanvasTkAgg(fig, master = self)  # Crea el area de dibujo en Tkinter
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=3)
        # ----------------------------------------------------------------------

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''
        
    def add_item_button_clicked(self):
        if self.controller:
            self.controller.add_item(['0',self.x_var.get(), self.y_var.get()])