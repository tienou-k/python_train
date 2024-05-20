# order.py

class Order:
    def __init__(self, products):
        self.products = products
        self.status = "pending"  # Status: pending, processing, completed

    def change_status(self, new_status):
        self.status = new_status
