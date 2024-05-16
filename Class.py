class serveur:
    def __init__(self, n):
        self.nom = n
        self.age = 20

    def afficher(self):
        print(self.nom)
obj = serveur('Okita')
print(f"Nom du serveur: {obj.nom}, Age: {obj.age}")