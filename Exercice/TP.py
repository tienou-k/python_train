import mysql.connector

def seconnecter_base():
        return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="commandeligne"
    )

class Utilisateur:
    """
    Classe de base pour représenter un utilisateur du système.
    """
    def enregistrer(self):
        """
        Methode
        """
        try:
            """
            connexion à la base de donnée MySQL
            """
            connexion = seconnecter_base()
            # Création d'un curseur pour exécuter des requêtes SQL
            cursor = connexion.cursor()
            # Exécution de la requête SQL pour insérer l'utilisateur dans la table des utilisateurs
            query = "INSERT INTO utilisateurs (nom, email, mot_de_passe) VALUES (%s, %s, %s)"
            cursor.execute(query, (self.nom, self.email, self.mot_de_passe))
            # Validation des changements dans la base de données
            connexion.commit()
            # Fermeture du curseur et de la connexion
            cursor.close()
            connexion.close()

            print("Utilisateur enregistré avec succès dans la base de données.")
        except mysql.connector.Error as error:
            print("Erreur lors de l'enregistrement de l'utilisateur dans la base de données:", error)

    def __init__(self, id, nom, email, mot_de_passe):
        """
        Constructeur de la classe Utilisateur.

        Args:
            nom (str): Le nom de l'utilisateur.
            email (str): L'adresse e-mail de l'utilisateur.
            mot_de_passe (str): Le mot de passe de l'utilisateur.
        """
        self.id = id
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe

def se_connecter(self):
    """
    Méthode permettant à l'utilisateur de se connecter au système.
    """
    try:
        # Connexion à la base de données pour vérifier l'authentification de l'utilisateur
        connexion = seconnecter_base()
        cursor = connexion.cursor()

        # Requête pour vérifier les informations d'identification de l'utilisateur dans la base de données
        query = "SELECT id, nom, email, mot_de_passe FROM utilisateurs WHERE email = %s"
        cursor.execute(query, (self.email,))
        utilisateur_data = cursor.fetchone()

        if utilisateur_data:
            id_utilisateur, nom_utilisateur, email_utilisateur, mot_de_passe_utilisateur = utilisateur_data
            if self.mot_de_passe == mot_de_passe_utilisateur:
                print("Connexion réussie.")
                self.id = id_utilisateur
                self.nom = nom_utilisateur
                return True
            else:
                print("Mot de passe incorrect.")
                return False
        else:
            print("Utilisateur non trouvé.")
            return False

    except mysql.connector.Error as error:
        print("Erreur lors de la connexion à la base de données:", error)
        return False
    finally:
        # Fermeture du curseur et de la connexion
        if connexion.is_connected():
            cursor.close()
            connexion.close()

    def se_déconnecter(self):
        """
        Méthode permettant à l'utilisateur de se déconnecter du système.
        """
        # Implémentation de la logique de déconnexion
        print("Déconnexion réussie.")
        # Remise à zéro des attributs d'utilisateur
        self.id = None
        self.nom = None
        self.email = None
        self.mot_de_passe = None


class Admin(Utilisateur):
    def __init__(self, id, nom, email, mot_de_passe):
        """
        Constructeur de la classe Utilisateur.

        Args:
            nom (str): Le nom de l'utilisateur.
            email (str): L'adresse e-mail de l'utilisateur.
            mot_de_passe (str): Le mot de passe de l'utilisateur.
        """
        self.id = id
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe

    def enregistrer(self):
        try:
            connexion = seconnecter_base()
            cursor = connexion.cursor()

            query = "INSERT INTO admin (id, nom, email, mot_de_passe) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.id, self.nom, self.email, self.mot_de_passe))

            connexion.commit()

            cursor.close()
            connexion.close()

            print("Admin enregistré avec succès dans la base de données.")
        except mysql.connector.Error as error:
            print("Erreur lors de l'enregistrement de l'admin dans la base de données:", error)

    def ajouter_produit(self, libelle, quantite, prix, date, categorie):

        # Implémentation de la logique d'ajout du produit (vérification des données, enregistrement en base de données)
        try:
            connexion = seconnecter_base()
            cursor = connexion.cursor()

            query = "INSERT INTO produit (libelle, quantite, prix, date, categorie) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (libelle, quantite, prix, date, categorie))

            connexion.commit()

            cursor.close()
            connexion.close()

            print("Produit enregistré avec succès dans la base de données.")
        except mysql.connector.Error as error:
            print("Erreur lors de l'enregistrement du produit dans la base de données:", error)

    def supprimer_produit(self, id_produit):

# Implémentation de la logique de suppression du produit (vérification des contraintes, suppression de la base de données)
        try:
            connexion = seconnecter_base()
            cursor = connexion.cursor()

            query = "DELETE FROM produit WHERE id_produit = %s"
            cursor.execute(query, (id_produit,))

            connexion.commit()

            cursor.close()
            connexion.close()

            print("Produit supprimé avec succès de la base de données.")
        except mysql.connector.Error as error:
            print("Erreur lors de la suppression du produit de la base de données:", error)

    def ajouter_personnel(self, nom, email, mot_de_passe):

# Implémentation de la logique d'ajout du membre du personnel (création du compte utilisateur, attribution des rôles)
        try:
            connexion = seconnecter_base()
            cursor = connexion.cursor()

            query = "INSERT INTO personnel (nom, email, mot_de_passe) VALUES (%s, %s, %s)"
            cursor.execute(query, (nom, email, mot_de_passe))

            connexion.commit()

            cursor.close()
            connexion.close()

            print("Personnel ajouté avec succès à la base de données.")
        except mysql.connector.Error as error:
            print("Erreur lors de l'ajout du personnel à la base de données:", error)

    def supprimer_personnel(self, id):
# Implémentation de la logique de suppression du membre du personnel (suppression du compte utilisateur)
        try:
            connexion = seconnecter_base()
            cursor = connexion.cursor()

            query = "DELETE FROM personnel WHERE id = %s"
            cursor.execute(query, (id,))

            connexion.commit()

            cursor.close()
            connexion.close()

            print("Personnel supprimé avec succès de la base de données.")
        except mysql.connector.Error as error:
            print("Erreur lors de la suppression du personnel de la base de données:", error)

    def supprimer_client(self, client):

# Implémentation de la logique de suppression du client (suppression du compte utilisateur, des commandes, etc.)
        try:
            connexion = seconnecter_base()
            cursor = connexion.cursor()

            query = "DELETE FROM produit WHERE id = %s"
            cursor.execute(query, (Client.id,))

            connexion.commit()

            cursor.close()
            connexion.close()

            print("Cleint supprimé avec succès de la base de données.")
        except mysql.connector.Error as error:
            print("Erreur lors de la suppression du client de la base de données:", error)

class Client(Utilisateur):
    def __init__(self, id, nom, email, mot_de_passe):
        """
        Constructeur de la classe Utilisateur.

        Args:
            nom (str): Le nom de l'utilisateur.
            email (str): L'adresse e-mail de l'utilisateur.
            mot_de_passe (str): Le mot de passe de l'utilisateur.
        """
        self.id = id
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        
    def enregistrer(self):
        try:
            connexion = seconnecter_base()
            cursor = connexion.cursor()

            query = "INSERT INTO client (id, nom, email, mot_de_passe) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.id, self.nom, self.email, self.mot_de_passe))

            connexion.commit()

            cursor.close()
            connexion.close()

            print("Client enregistré avec succès dans la base de données.")
        except mysql.connector.Error as error:
            print("Erreur lors de l'enregistrement du client dans la base de données:", error)

    def ajouter_au_panier(self, produit, quantite):
        """
        Méthode permettant au client d'ajouter un produit au panier.

        Args:
            produit (Produit): Le produit à ajouter.
            quantité (int): La quantité du produit à ajouter.
        """
        if produit.nom in self.panier:
            self.panier[produit.nom] += quantite
        
            if self.panier is None:
                self.panier = Panier(self)
                self.panier.ajouter_produit(produit, quantite)
        else:
            self.panier[produit.nom] = quantite
    def afficher_panier(self):
        """
        Méthode permettant au client d'afficher son panier.
        """
        if self.panier is None:
            print("Votre panier est vide.")
        else:
            self.panier.afficher_details()

    def passer_commande(self, mode_paiement, adresse_livraison):
        """
        Méthode permettant au client de passer une commande à partir de son panier.

        Args:
            mode_paiement (str): Le mode de paiement choisi.
            adresse_livraison (str): L'adresse de livraison de la commande.
        """
        if self.panier is None or len(self.panier.produit) == 0:
            print("Votre panier est vide. Vous ne pouvez pas passer de commande.")
            return
        commande = Commande(self, self.panier.produit, mode_paiement, adresse_livraison)
        # Traitement de la commande (enregistrement, paiement, etc.)
        # ...
        self.panier = None  # Vider le panier après la commande

    def afficher_commandes(self):
        """
        Méthode permettant au client d'afficher ses commandes.
        """
        # Implémentation de la logique d'affichage des commandes du client
        pass
    def supprimer(self):
        """
        Méthode permettant de supprimer l'enregistrement du personnel de la base de données.
        """
        try:
            connexion = seconnecter_base()
            cursor = connexion.cursor()

            query = "DELETE FROM client WHERE id = %s"
            cursor.execute(query, (self.id,))

            connexion.commit()

            cursor.close()
            connexion.close()

            print("Client supprimé avec succès de la base de données.")
        except mysql.connector.Error as error:
            print("Erreur lors de la suppression du client de la base de données:", error)

class Personnel(Utilisateur):
    """
    Classe dérivée représentant un membre du personnel du système.
    Héritière de la classe Utilisateur.
    """
    def __init__(self, id, nom, email, mot_de_passe):
        """
        Constructeur de la classe Utilisateur.

        Args:
            nom (str): Le nom de l'utilisateur.
            email (str): L'adresse e-mail de l'utilisateur.
            mot_de_passe (str): Le mot de passe de l'utilisateur.
        """
        self.id = id
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe
        
    def enregistrer(self):
        try:
            connexion = seconnecter_base()
            cursor = connexion.cursor()

            query = "INSERT INTO personnel (id, nom, email, mot_de_passe) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.id, self.nom, self.email, self.mot_de_passe))

            connexion.commit()

            cursor.close()
            connexion.close()

            print("Personnel enregistré avec succès dans la base de données.")
        except mysql.connector.Error as error:
            print("Erreur lors de l'enregistrement du personnel dans la base de données:", error)

    def traiter_commandes(self, commande):
        """
        Méthode permettant au personnel de traiter une commande.

        Args:
            commande (Commande): La commande à traiter.
        """
        # Implémentation de la logique de traitement de la commande (vérification du stock, préparation de l'expédition)
        pass


class Produit:
    """
    Classe représentant un produit du système.
    """
    # def enregistrer(self):
    #     try:
    #         connexion = seconnecter_base()
    #         cursor = connexion.cursor()

    #         query = "INSERT INTO client (id_produit, libelle, quantite, date, prix, categorie) VALUES (%s, %s, %s, %s, %s, %s)"
    #         cursor.execute(query, (self.id_produit, self.libelle, self.quantite, self.date, self.prix, self.categorie))

    #         connexion.commit()

    #         cursor.close()
    #         connexion.close()

    #         print("Proudit enregistré avec succès dans la base de données.")
    #     except mysql.connector.Error as error:
    #         print("Erreur lors de l'enregistrement du produit dans la base de données:", error)

    def __init__(self, id_produit, libelle, quantite, date, prix, categorie):
        """
        Constructeur de la classe Produit.

        Args:
            nom (str): Le nom du produit.
            description (str): La description du produit.
            prix (float): Le prix du produit.
            categorie (Categorie): La catégorie du produit.
        """
        self.id_produit = id_produit
        self.libelle = libelle
        self.quantite = quantite
        self.date = date
        self.prix = prix
        self.categorie = categorie

    def ajouter_au_panier(self, client, quantite):
        """
        Méthode permettant d'ajouter le produit au panier d'un client donné.

        Args:
            client (Client): Le client auquel le produit doit être ajouté.
            quantité (int): La quantité du produit à ajouter.
        """
        if quantite <= 0:
            raise ValueError("La quantité doit être un nombre positif")
        if client is None:
            raise ValueError("Le client ne peut pas être None")

        client.ajouter_au_panier(self, quantite)

    def afficher_details(self):
        """
        Méthode permettant d'afficher les détails du produit.
        """
        print(f"Libelle: {self.libelle}")
        print(f"Prix: {self.prix}")
        print(f"quantite: {self.quantite}")
        print(f"date: {self.date}")
        print(f"Catégorie: {self.categorie.nom}")
        
        Produit.afficher_details()
        # Appelez la méthode afficher_details sur l'instance de produit
        produit.afficher_details()

        
    def sauvegarder(self):
        produit_id = self.get_produit_id()

        # Maintenant, vous pouvez insérer le produit dans la table de catégorie respective
        self.inscrire_dans_categorie(produit_id)

    def inscrire_dans_categorie(self, produit_id, categorie_id):
        self.produit_id = produit_id
        self.categorie_id = categorie_id
        categorie_id = self.get_categorie_id()



class Categorie:
    """
    Classe représentant une catégorie de produit dans le système.
    """
    def enregistrer(self):
        try:
            connexion = seconnecter_base()
            cursor = connexion.cursor()

            query = "INSERT TO Categorie (id, nom,) VALUES (%s, %s)"
            cursor.execute(query, (self.id, self.nom))

            connexion.commit()

            cursor.close()
            connexion.close()

            print("Categorie enregistré avec succès dans la base de données.")
        except mysql.connector.Error as error:
            print("Erreur lors de l'enregistrement du categorie dans la base de données:", error)

    def __init__(self, id, nom):
        """
        Constructeur de la classe Catégorie.

        Args:
            nom (str): Le nom de la catégorie.
        """
        self.id = id
        self.nom = nom
        self.produit = {} 

    def ajouter_produit(self, produit):
        """
        Méthode permettant d'ajouter un produit à la catégorie.

        Args:
            produit (Produit): Le produit à ajouter.
        """
        self.produit[produit.nom] = produit

    def supprimer_produit(self, nom_produit):
        """
        Méthode permettant de supprimer un produit de la catégorie.

        Args:
            nom_produit (str): Le nom du produit à supprimer.
        """
        if nom_produit in self.produit:
            del self.produit[nom_produit]

    def afficher_arborescence(self):
        """
        Méthode permettant d'afficher l'arborescence des catégories et sous-catégories, y compris les produit.
        """
        def afficher_rec(categorie, indent=0):
            print(f"{' ' * indent}{categorie.nom}")
            for sous_categorie in categorie.sous_categories.values():
                afficher_rec(sous_categorie, indent + 2)
            for produit in categorie.produit.values():
                print(f"{' ' * (indent + 2)}- {produit.nom}")

        afficher_rec(self)
        
    def sauvegarder(self):
        categorie_id = self.get_categorie_id()

        return categorie_id

class Commande:
    """
    Classe représentant une commande dans le système.
    """
    def enregistrer(self):
        try:
            connexion = seconnecter_base()
            cursor = connexion.cursor()

            query = "INSERT INTO client (id, nom, email, mot_de_passe) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.id, self.client, self.produit, self.mode_paiement, self.adresse_livraison))

            connexion.commit()

            cursor.close()
            connexion.close()

            print("Commande enregistré avec succès dans la base de données.")
        except mysql.connector.Error as error:
            print("Erreur lors de l'enregistrement de la commande dans la base de données:", error)
            
    def __init__(self, id, client, produit, mode_paiement, adresse_livraison):
        """
        Constructeur de la classe Commande.

        Args:
            client (Client): Le client ayant passé la commande.
            produit (list): La liste des produit commandés.
            mode_paiement (str): Le mode de paiement utilisé.
            adresse_livraison (str): L'adresse de livraison de la commande.
        """
        self.id = id
        self.client = client
        self.produit = produit
        self.mode_paiement = mode_paiement
        self.adresse_livraison = adresse_livraison
        self.statut = "En cours"  # Statut initial de la commande

    def confirmer(self):
        """
        Méthode permettant de confirmer la commande.
        """
        # Implémentation de la logique de confirmation de la commande (vérification du stock, etc.)
        self.statut = "Confirmée"

    def expédier(self):
        """
        Méthode permettant d'expédier la commande.
        """
        # Implémentation de la logique d'expédition de la commande (mise à jour du statut, envoi de notification)
        self.statut = "Expédiée"

    def afficher_details(self):
        """
        Méthode permettant d'afficher les détails de la commande.
        """
        print(f"Client: {self.client.nom}")
        print(f"Produit:")
        for produit in self.produit:
            print(f"- {produit.nom}")
        print(f"Mode de paiement: {self.mode_paiement}")
        print(f"Adresse de livraison: {self.adresse_livraison}")
        print(f"Statut: {self.statut}")

class Panier:
    """
    Classe représentant un panier d'achat dans le système.
    """

    def __init__(self, client):
        """
        Constructeur de la classe Panier.

        Args:
            client (Client): Le client associé au panier.
        """
        self.client = client
        self.produit = []  # Liste des produit dans le panier

    def ajouter_produit(self, produit, quantité):
        """
        Méthode permettant d'ajouter un produit au panier.

        Args:
            produit (Produit): Le produit à ajouter.
            quantité (int): La quantité du produit à ajouter.
        """
        # Vérifier si le produit est déjà dans le panier et mettre à jour la quantité si nécessaire
        self.produit.append((produit, quantité))

    def supprimer_produit(self, produit):
        """
        Méthode permettant de supprimer un produit du panier.

        Args:
            produit (Produit): Le produit à supprimer.
        """
        self.produit = [p for p in self.produit if p[0] != produit]

    def calculer_total(self):
        """
        Méthode permettant de calculer le total du panier.

        Returns:
            float: Le total du panier (somme des prix des produit multipliés par leurs quantités).
        """
        total = 0
        for produit, quantité in self.produit:
            total += produit.prix * quantité
        return total

    def afficher_details(self):
        """
        Méthode permettant d'afficher les détails du panier.
        """
        print(f"Client: {self.client.nom}")
        print(f"Produit:")
        for produit, quantité in self.produit:
            print(f"- {produit.nom} (x{quantité})")
        print(f"Total: {self.calculer_total()}")

class Paiement:
    """
    Classe représentant un paiement dans le système.
    """
    def enregistrer(self):
        try:
            connexion = seconnecter_base()
            cursor = connexion.cursor()

            query = "INSERT INTO client (id, nom, email, mot_de_passe) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.id, self.mode_paiement, self.montant,))

            connexion.commit()

            cursor.close()
            connexion.close()

            print("Client enregistré avec succès dans la base de données.")
        except mysql.connector.Error as error:
            print("Erreur lors de l'enregistrement du client dans la base de données:", error)
    def __init__(self, id, mode_paiement, montant):
        """
        Constructeur de la classe Paiement.

        Args:
            mode_paiement (str): Le mode de paiement utilisé.
            montant (float): Le montant du paiement.
        """
        self.id = id
        self.mode_paiement = mode_paiement
        self.montant = montant

    def traiter(self):
        """
        Méthode permettant de traiter le paiement (simulation ou intégration avec un système de paiement externe).

        Returns:
            bool: True si le paiement a réussi, False sinon.
        """
        # Implémentation de la logique de traitement du paiement
        # ...
        return True  # Exemple de retour de succès

admin = Admin(id=1, nom="Admin", email="admin@example.com", mot_de_passe="admin123")    
# Créez une instance de la classe Produit
produit = Produit(
    id_produit= 2, 
    libelle="Tomate", 
    prix=50.0, 
    quantite=10, 
    date="2024-05-10", 
    categorie= Categorie(id = 2, nom="Électronique"))




# Appel aux méthode ajouter, supprimer et modifier
