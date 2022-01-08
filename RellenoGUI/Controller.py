class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # save the model
            self.model.email = email
            self.model.save()

            # show a success message
            self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)
            
    def add_item(self, item_tree):
        try:
            self.model.item_tree = item_tree
            print(self.model.item_tree)
        except ValueError as error:
            self.view.show_error(error)
    