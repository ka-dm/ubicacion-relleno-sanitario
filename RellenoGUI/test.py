import random
import statistics
from minizinc import Instance, Model, Solver

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
      
def execute_mzn_file(data):
    
    #print("Ejecutar mzn")
    src = "./MiniZnFiles/RellenoFloat.mzn"
    relleno = Model(src)
    solver = Solver.lookup("coin-bc")
    relleno.add_string(data)
    instance = Instance(solver, relleno)
    result = instance.solve()
    #print('Rusultado mzn >>> \n', result, '>>>')
    return {'x': result["x"], 'y':  result["y"],'f':  result["f"], 'time': result.statistics['solveTime']}

def generar_ciudades_aleatorias(m, n):
        if (m < (n+1)*(n+1)):
            ciudaes = []
            x_ciud = []
            y_ciud = []
            for i in range(m):
                x = random.randint(0,n)
                y = random.randint(0,n)
                while ([x,y] in ciudaes):
                    x = random.randint(0,n)
                    y = random.randint(0,n)
                ciudaes.append([x,y])
                x_ciud.append(x)
                y_ciud.append(y)
                
            #ciudaes = np.array(ciudaes).flatten()
            #data = {'n': n,'m': m,'ciudades': ciudaes}
            return x_ciud, y_ciud
        else:
            print("Error: m > n+1*n+1")

def generate_dzm_content(x,y, n):
        cadena = 'n='+ str(n) + '; \n' +'m=' + str(len(x)) + '; \n' +  'ciudades=['
        for i in range(len(x)):
            line = "|"+str(x[i])+","+str(y[i])
            if (i == len(x)-1):
                cadena = cadena + line + "|];"
            else:
                cadena = cadena + line  + " \n"
        return cadena

def pruebas():
    times = []
    tam = [350]
    cant_pruebas = 3
    
    for j in range(len(tam)):
        promedios = []
        for i in range(cant_pruebas):
            x, y = generar_ciudades_aleatorias(tam[j], tam[j])
            data = generate_dzm_content(x,y, tam[j])
            time = execute_mzn_file(data)['time']
            print(' Timepo ', i ,'= ',time.total_seconds())
            times.append(time.total_seconds())   
        mean = sum(times)/len(times)
        promedios.append(mean)
        print('Prueba', j,' tam =', tam[j],', promedio = ',mean)
    print('Promedios: ', promedios)
    graficar_resultados(tam, promedios)
    
    

def graficar_resultados(x, y):
    mymodel = np.poly1d(np.polyfit(x, y, 3))

    myline = np.linspace(1, 22, 100)

    plt.scatter(x, y)
    plt.plot(myline, mymodel(myline))
    plt.show()

    
    
if __name__ == '__main__':
    #pruebas()
    graficar_resultados([5, 10, 50, 100, 150, 175, 200, 250, 300, 350], 
                        [0.334, 0.565, 6.866, 22.279, 43.266, 45.337 ,78.196, 91.463, 183.236, 310.625])