import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


def create_input_frame(container):

    frame = ttk.Frame(container)
    frame['borderwidth'] = 5
    frame['relief'] = 'sunken'

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # Tamaño de region
    ttk.Label(frame, text='Tamaño de region: ').grid(column=0, row=0, sticky=tk.W)
    keyword = ttk.Entry(frame, width=10)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=5)

    return frame


def create_button_frame(container):
    frame = ttk.Frame(container)
    frame['borderwidth'] = 5
    frame['relief'] = 'sunken'

    alignment_var = tk.StringVar()
    alignments = ('Left', 'Center', 'Right')

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Ejecutar').grid(column=0, row=1)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=3)

    return frame


def crate_lf(container):
    
    # label frame
    lf = ttk.LabelFrame(container, text='Coordenadas')
    lf.grid(column=0, row=0, padx=20, pady=20)

    # Coordenada x:
    ttk.Label(lf, text='X: ').grid(column=0, row=0, sticky=tk.W)
    current_value_x = tk.StringVar(value=0)
    spin_box_x = ttk.Spinbox(lf,width=10 , from_=0, to=30, textvariable=current_value_x, wrap=True)
    spin_box_x.grid(column=0, row=1)

    # Coordenada y:
    ttk.Label(lf, text='Y: ').grid(column=1, row=0, sticky=tk.W)
    current_value_y = tk.StringVar(value=0)
    spin_box_y = ttk.Spinbox(lf,width=10 , from_=0, to=30, textvariable=current_value_y, wrap=True)
    spin_box_y.grid(column=1, row=1)

    # Añadir punto:
    ttk.Button(lf, text='Añadir punto').grid(column=0, row=3)
    
    return lf

def create_table_frame(container):
    
    # label frame
    label_frame = ttk.LabelFrame(container, text='Tabla')
    label_frame.grid(column=0, row=0, padx=20, pady=20)

    # define columns
    columns = ('ciudad', 'este', 'norte')
    tree = ttk.Treeview(label_frame, columns=columns, show='headings')

    # customice columns
    width_col = 50
    tree.column('ciudad', width=width_col, anchor=tk.W)
    tree.column('este', width=width_col, anchor=tk.W)
    tree.column('norte', width=width_col, anchor=tk.CENTER)

    # define headings
    tree.heading('ciudad', text='Ciudad')
    tree.heading('este', text='Este')
    tree.heading('norte', text='Norte')
    
    # generate sample data
    contacts = []
    for n in range(1, 10):
        x = round(random.random() * 10)
        y = round(random.random() * 10)
        contacts.append((f'{n}', f'{x}', f'{y}'))

    # add data to the treeview
    for contact in contacts:
        tree.insert('', tk.END, values=contact)


    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))


    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')

    # add a scrollbar
    scrollbar = ttk.Scrollbar(label_frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    return label_frame  

def create_main_window():

    # root window
    root = tk.Tk()
    root.title('Replace')
    root.geometry('800x600')
    root.resizable(1, 1)
    # windows only (remove the minimize/maximize button)
    root.attributes('-toolwindow', True)

    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    lb_frame = crate_lf(root)
    lb_frame.grid(column=0, row=2)

    table_frame = create_table_frame(root)
    table_frame.grid(column=0, row=3)

    button_frame = create_button_frame(root)
    button_frame.grid(column=0, row=4)

    root.mainloop()


if __name__ == "__main__":
    create_main_window()