from tkinter import Tk
from tkinter import filedialog


class Controller:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.cont_item = 0

    def save(self):
        try:
            x,y = self.get_data_tree()
            data = self.generate_dzm_content(x,y, self.get_tam_area())
        except ValueError as error:
            # show an error message
            self.view.show_error(error)
    
    def import_data(self):
        try:
            src = filedialog.askopenfilename(initialdir = "C:/Users/kevin/Documents/ProyectoUbicacionRelleno/MiniZnFiles/Datos-20220111",
                                            title = "Select file",
                                            filetypes = [("dzn files","*.dzn")])
            data = self.model.import_data(src)
            self.set_data_tree(data)
            x_array, y_array = self.get_data_tree()
            self.view.set_text(self.view.tam_area_entry, data['n'])
            self.view.graficar(data['n'], x_array, y_array)
        except ValueError as error:
            # show an error message
            self.view.show_error(error)
            
    def get_tam_area(self):
        print(self.model.tam_area)
        return self.model.tam_area
            
    def add_item(self, item_tree, tam_area):
        try:
            self.model.item_tree = item_tree
            item_tree[0] = self.cont_item
            self.cont_item += 1
            self.view.tree.insert('', 'end', values=item_tree)
            self.model.tam_area = tam_area
            
            #print(self.model.item_tree)
            #print(self.model.tam_area)
        except ValueError as error:
            self.view.show_error(error)
    
    def set_data_tree(self, data):
        self.celar_data_tree()
        for i in range(0 , len(data['ciudades']), 2):
            este = data['ciudades'][i]
            norte = data['ciudades'][i+1]
            self.add_item(['0',data['ciudades'][i],data['ciudades'][i+1]], data['n'])
        
    def celar_data_tree(self):
        for i in self.view.tree.get_children():
            self.view.tree.delete(i)
    
    def get_data_tree(self):
        x = []
        y = []
        
        for line in self.view.tree.get_children():
            x.append(self.view.tree.item(line)['values'][1])
            y.append(self.view.tree.item(line)['values'][2])
        return x,y
    
    def generate_dzm_content(self,x,y, n):
        cadena = 'n='+ str(n) + '; \n' +'m=' + str(len(x)) + '; \n' +  'ciudades=['
        for i in range(len(x)):
            line = "|"+str(x[i])+","+str(y[i])
            if (i == len(x)-1):
                cadena = cadena + line + "|];"
            else:
                cadena = cadena + line  + " \n"
        self.model.save_data(cadena)
        #print(cadena)
        self.extract_dzm_content()
        
    def extract_dzm_content(self):
        #datos = self.model.read_data()
        #lineas = datos.split(';')
        #print(lineas)
        print("extract_dzm_content")
        
        
                