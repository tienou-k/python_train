# tests.py
from admin import Admin
from product import Product
from category import Category
from admin import Admin
from client import Client



role = input("Veuillez spécifier votre rôle (admin/client/personnel) : ")

# Vérifier le rôle de l'utilisateur et afficher les fonctionnalités correspondantes
class role:
    def fonct():
        if role.lower() == 'admin':
            print("Fonctionnalités disponibles pour l'admin :")
            print("1. Ajouter un produit")
            print("2. Supprimer un produit")
            print("3. Ajouter une catégorie")
            print("4. Supprimer une catégorie")
            print("5. Ajouter du personnel")
            print("6. Supprimer du personnel")
            print("7. Bannir un client du système")
    afficher = fonct()   
    # L'admin peut ajouter, supprimer, modifier, etc.
choice = input("Veuillez choisir une fonctionnalité : ")
admin = Admin()

if choice == '1':
        # Ajouter un produit
    name = input("Nom du produit : ")
    price = input("Prix du produit : ")
    quantity = input("Quantité du produit : ")
    date = input("Date d'ajout du produit : ")
    category = input("Categorie du produit :" )
    product1 = Product(name, price, quantity, date, category)
    admin.add_product(name, price, quantity, date, category)
    print("Produit ajouté avec succès.")
