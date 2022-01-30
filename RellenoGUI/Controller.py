
import random
from tkinter import Tk
from tkinter import filedialog
from unittest import result
from minizinc import Instance, Model, Solver

class Controller:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.cont_item = 0

    def save(self):
        try:
            x,y = self.get_data_tree()
            data = self.generate_dzm_content(x,y, self.get_tam_area())
            este, norte, dist = self.execute_mzn_file()
            index_ciudad = -1
            for i in range(len(x)):
                dist_manhattan = abs(x[i] - este) + abs(y[i] - norte)
                if (dist_manhattan == dist):
                    print("Ciudad ",i+1," x=", x[i], " y=", y[i])
                    index_ciudad = i
            self.view.graficar(int(self.get_tam_area()), x, y, 
                               relleno_x= este, relleno_y=norte ,solucion=True,
                               index_ciudad = index_ciudad)
        except ValueError as error:
            # show an error message
            self.view.show_error(error)
    
    def import_data(self):
        try:
            src = filedialog.askopenfilename(initialdir = "./MiniZnFiles/Datos-20220111",
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
        #print("get_tam_area = ",self.model.tam_area)
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
      
    def execute_mzn_file(self):
        #print("Ejecutar mzn")
        src = "./MiniZnFiles/RellenoFloat.mzn"
        relleno = Model(src)
        solver = Solver.lookup("coin-bc")
        relleno.add_file("./Datos.dzn")
        instance = Instance(solver, relleno)
        result = instance.solve()
        print( 'Rusultado mzn >>> Este = ',result["x"], ' Norte = ',result["y"], ' f = ',result["f"])
        return result["x"], result["y"], result["f"]
        
    def generar_ciudades(self, m, n):
        if (m <= n):
            ciudades = []
            for i in range(m):
                x = random.randint(0,n)
                y = random.randint(0,n)
                while ([x,y] in ciudades):
                    x = random.randint(0,n)
                    y = random.randint(0,n)
                ciudades.append([x,y])
            return ciudades
        else: 
            return "Eror: no se puede generar ciudades con una cantidad de ciudades mayor a la cantidad de area"
    
    
    
        
        
        
            
            
            
        
        
            

        
                