### Admin peut :

## commande d'ajout un produit

admin = Admin(id=1, nom="Admin", email="admin@example.com", mot_de_passe="admin123")
admin.ajouter_produit(libelle="Nouveau produit", quantite=10, prix=50.0, date="2024-05-10", categorie="Electronique")

## supprimer un produit

admin.supprimer_produit(id_produit=1)

# ajout personnel

admin = Admin(id=admin_id, nom="Admin", email="admin@example.com", mot_de_passe="admin_password")

# Appel de la méthode ajouter_personnel avec les informations du personnel à ajouter

nom_personnel = "Nom du personnel"
email_personnel = "email@example.com"
mot_de_passe_personnel = "mot_de_passe_du_personnel"

admin.ajouter_personnel(nom_personnel, email_personnel, mot_de_passe_personnel)

# supprimer personnel

admin.supprimer_personnel(id)

admin.supprimer_client(id_client=1)
