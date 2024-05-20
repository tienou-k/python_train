# client.py
from user import User

class Client(User):
    def __init__(self):
        super().__init__('client')
        self.products_in_cart = []
        self.orders = []

    # Ajoutez les méthodes pour gérer le panier, passer des commandes, etc.
