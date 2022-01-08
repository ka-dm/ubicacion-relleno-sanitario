class Controller:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.cont_item = 0

    def save(self):
        try:
            self.model.save_data()
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
            print(self.model.item_tree)
            #print(self.model.tam_area)
        except ValueError as error:
            self.view.show_error(error)
    
    