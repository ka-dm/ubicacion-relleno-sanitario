import tkinter as tk
from tkinter import ttk

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(self, text='Email:')
        self.label.grid(row=1, column=0)

        # email entry
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # save button
        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        # set the controller
        self.controller = None
        
        # add item button
        self.add_item_button = ttk.Button(self, text='Add Item', command=self.add_item_button_clicked)
        self.add_item_button.grid(row=3, column=0, padx=10)
        
        # entry x
        self.x_var = tk.StringVar()
        self.x_entry = ttk.Entry(self, textvariable=self.x_var, width=10)
        self.x_entry.grid(row=3, column=1, sticky=tk.NSEW)
        
        # entry y
        self.y_var = tk.StringVar()
        self.y_entry = ttk.Entry(self, textvariable=self.y_var, width=10)
        self.y_entry.grid(row=3, column=2, sticky=tk.NSEW)
        
        # treeview -------------------------------------------------------------
        # define columns
        self.columns = ('1', '2', '3')

        self.tree = ttk.Treeview(self, columns=self.columns, show='headings')
        
        # define headings
        self.tree.heading('1', text='Ciudad')
        self.tree.heading('2', text='Este')
        self.tree.heading('3', text='Norte')
        
        self.tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
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
            self.tree.insert('', 'end', values=['0',self.x_var.get(), self.y_var.get()])