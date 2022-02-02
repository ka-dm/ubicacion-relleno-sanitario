
import random
import statistics
from tkinter import Tk
from tkinter import filedialog
import tkinter
from unittest import result
from minizinc import Instance, Model, Solver
import numpy as np

class Controller:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.cont_item = 0

    def save(self):
        try:
            x,y = self.get_data_tree()
            data = self.generate_dzm_content(x,y, self.get_tam_area())
            output_mzn =  self.execute_mzn_file()
            este = output_mzn['x']
            norte = output_mzn['y']
            dist = output_mzn['f']
            time = output_mzn['time']
            index_ciudad = -1
            for i in range(len(x)):
                dist_manhattan = abs(x[i] - este) + abs(y[i] - norte)
                if (dist_manhattan == dist):
                    print("Ciudad ",i+1," x=", x[i], " y=", y[i])
                    index_ciudad = i
            self.view.graficar(int(self.get_tam_area()), x, y, 
                               relleno_x= este, relleno_y=norte ,solucion=True,
                               index_ciudad = index_ciudad)
            #print('Timepo de ejecucion:', time)
            self.view.text_output.delete(1.0, tkinter.END)
            self.view.text_output.insert(tkinter.END, 
                " Este " + str(round(este,4)) + "\n " +
                "Norte " + str(round(norte,4)) + "\n " +
                "Distancia " + str(round(dist,4)))
            
            return time
        except ValueError as error:
            # show an error message
            self.view.show_error(error)
    
    def import_data(self):
        try:
            src = filedialog.askopenfilename(initialdir = "./",
                                            title = "Select file",
                                            filetypes = [("dzn files","*.dzn")])
            data = self.model.import_data(src)
            self.set_data_tree(data)
            print(type(data), data)
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
        self.clear_data_tree()
        for i in range(0 , len(data['ciudades']), 2):
            este = data['ciudades'][i]
            norte = data['ciudades'][i+1]
            self.add_item(['0',data['ciudades'][i],data['ciudades'][i+1]], data['n'])
        
    def clear_data_tree(self):
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
      
    def execute_mzn_file(self, src_data = './Datos.dzn'):
        #print("Ejecutar mzn")
        src = "./MiniZnFiles/RellenoFloat.mzn"
        relleno = Model(src)
        solver = Solver.lookup("coin-bc")
        relleno.add_file(src_data)
        instance = Instance(solver, relleno)
        result = instance.solve()
        #print( 'Rusultado mzn >>> Este = ',result["x"], ' Norte = ',result["y"], ' f = ',result["f"])
        print('Rusultado mzn >>> \n', result, '>>>')
        return {'x': result["x"], 'y':  result["y"],'f':  result["f"], 'time': result.statistics['solveTime']}
        
    def generar_ciudades_aleatorias(self, m, n):
        if (m < (n+1)*(n+1)):
            ciudaes = []
            for i in range(m):
                x = random.randint(0,n)
                y = random.randint(0,n)
                while ([x,y] in ciudaes):
                    x = random.randint(0,n)
                    y = random.randint(0,n)
                ciudaes.append([x,y])
            ciudaes = np.array(ciudaes).flatten()
            data = {'n': n,'m': m,'ciudades': ciudaes}
            self.set_data_tree(data)
            x_array, y_array = self.get_data_tree()
            self.view.graficar(data['n'], x_array, y_array)
            return data
        else:
            print("Error: m > n+1*n+1")
    
    def aux_generar_ciudades_aleatorias(self, m, n):
        ciudaes = []
        for i in range(m):
            x = random.randint(0,n)
            y = random.randint(0,n)
            while ([x,y] in ciudaes):
                x = random.randint(0,n)
                y = random.randint(0,n)
                ciudaes.append([x,y])
                
        print(ciudaes)
        ciudaes = np.array(ciudaes).flatten()
        return {'n': n,'m': m,'ciudades': ciudaes}
            
    def pruebas(self):
        times = []
        tam = [5,10,50,100,500,1000]
        cant_pruebas = 3
        
        for j in range(len(tam)):
            for i in range(cant_pruebas):
                data = self.generar_ciudades_aleatorias(tam[j], tam[j])
                time = self.save()
            times.append(time)   
            #mean = statistics.mean(times)
            mean = 0
            print('Prueba', i,' promedio = ',mean, '\n', times)
        
            
            
            
        
        
            

        
                