class Categorie:
    # Classe représentant une catégorie de produit dans le système.

    def __init__(self, id_categorie, nom):
        self.id = id_categorie
        self.nom = nom
    def tostring(self):
        print(self.id_categorie, self.nom)
def ajouter_categorie(liste_categories, id_categorie, nom):
    # Crée une nouvelle instance de Categorie et l'ajoute à la liste de catégories
    nouvelle_categorie = Categorie(id_categorie, nom)
    liste_categories.append(nouvelle_categorie)

def supprimer_categorie(liste_categories, id_categorie):
    # Parcourt la liste de catégories et supprime la catégorie correspondant à l'ID spécifié
    for categorie in liste_categories:
        if categorie.id == id_categorie:
            liste_categories.remove(categorie)
            break  # Sortie de la boucle une fois que la catégorie est trouvée et supprimée


# Créer une liste pour stocker les catégories
liste_categories = []

# Ajouter une nouvelle catégorie
ajouter_categorie(liste_categories, id_categorie=1, nom="Electronique")


# Vérifier le contenu de la liste des catégories après la suppression
print(liste_categories)  # Output: []


