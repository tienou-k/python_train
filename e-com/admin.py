# admin.py
from user import User
from product import Product
from category import Category

class Admin(User):
    def __init__(self):
        super().__init__('admin')
        self.personnel = []
        self.clients = []
        self.products = []
        self.categories = []

    def add_personnel(self, personnel):
        self.personnel.append(personnel)

    def remove_personnel(self, personnel):
        self.personnel.remove(personnel)

    def add_client(self, client):
        self.clients.append(client)

    def remove_client(self, client):
        self.clients.remove(client)

    def add_product(self,name, price, quantity, date, category):
        # Vérifier si la catégorie existe déjà
        category = next((c for c in self.categories if c.name == category), None)

        # Si la catégorie n'existe pas, la créer
        if category is None:
            category = Category(category)
            self.categories.append(category)

        # Ajouter le produit à la catégorie
        product = Product(name, price, quantity, date, category)
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def modify_product(self, product, new_name, new_price, new_quantity, new_date, new_category):
        if product in self.products:
            product.name = new_name
            product.price = new_price
            product.quantity = new_quantity
            product.date = new_date
            product.category = new_category

    def add_category(self, category):
        self.categories.append(category)

    def remove_category(self, category):
        self.categories.remove(category)
