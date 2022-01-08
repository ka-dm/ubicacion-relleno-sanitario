import re

class Model:
    def __init__(self, email, item_tree, tam_area):
        self.email = email
        self.item_tree = item_tree
        self.tam_area = tam_area

    @property
    def email(self):
        return self.__email
    
    @property
    def item_tree(self):
        return self.__item_tree
    
    @property
    def tam_area(self):
        return self.__tam_area

    @email.setter
    def email(self, value):
        """
        Validate the email
        :param value:
        :return:
        """
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')
        
    @item_tree.setter
    def item_tree(self, value):
        self.__item_tree = value

    @tam_area.setter
    def tam_area(self, value):
        self.__tam_area = value

    def save(self):
        """
        Save the email into a file
        :return:
        """
        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')

    def save_data(self):
        """
        save an item into the tree
        :return:
        """
        with open('Datos.txt', 'a') as f:
            f.write(self.item_tree + '\n')