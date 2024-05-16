# personnel.py
from user import User

class Personnel(User):
    def __init__(self):
        super().__init__('personnel')

    # Vous pouvez ajouter des méthodes spécifiques pour gérer les commandes des clients, etc.
