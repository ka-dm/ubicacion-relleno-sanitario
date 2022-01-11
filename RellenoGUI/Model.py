from pymzn import dzn

class Model:
    def __init__(self):
        self.item_tree = []
        self.tam_area = 10

    @property
    def item_tree(self):
        return self.__item_tree
    
    @property
    def tam_area(self):
        return self.__tam_area
        
    @item_tree.setter
    def item_tree(self, value):
        self.__item_tree = value

    @tam_area.setter
    def tam_area(self, value):
        self.__tam_area = value

    def save_data(self, data):
        with open("Datos.dzn", "w") as f:
            #f.write("\n".join(data))
            f.write(data)
    
    def read_data(self):
        with open('Datos.dzn', 'r') as f:
            cadena = f.read()
        return cadena

        