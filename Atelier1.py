
titre = "L'Étranger"
auteur = "Albert Camus"
prix = 120.0
quantite = 5

print(f"Le livre '{titre}' de {auteur} coûte {prix} DH.")

cout_total = prix * quantite
print(f"Le coût total du stock est de : {cout_total} DH.")

nouveau_prix = prix * 1.10
print(f"Le nouveau prix après une augmentation de 10% est de : {nouveau_prix} DH.")
# Listes de base fournies
livres = ["L'Étranger", "1984", "Le Petit Prince", "Les Misérables"]
prix = [120.0, 150.0, 90.0, 200.0]
auteurs = ["Albert Camus", "George Orwell", "Antoine de Saint-Exupéry", "Victor Hugo"]


print("Deuxième livre :", livres[1])

livres.append("Alchimist")
print("Liste des livres mise à jour :", livres)

livres.remove("1984")
print("Liste après suppression de '1984' :", livres)

livre_tuple = ("L'Étranger", "Albert Camus", 120.0)
print("\nÉléments du tuple livre :")
print("Titre :", livre_tuple[0])
print("Auteur :", livre_tuple[1])
print("Prix :", livre_tuple[2], "DH")

bibliotheque_liste = [
    ("L'Étranger", "Albert Camus", 120.0),
    ("1984", "George Orwell", 150.0),
    ("Le Petit Prince", "Antoine de Saint-Exupéry", 90.0),
    ("Les Misérables", "Victor Hugo", 200.0)
]
print("\nBibliothèque sous forme de liste de tuples :")
print(bibliotheque_liste)


bibliotheque = {
    "L'Étranger": ("L'Étranger", "Albert Camus", 120),
    "1984": ("1984", "George Orwell", 150),
    "Le Petit Prince": ("Le Petit Prince", "Antoine de Saint-Exupéry", 90)
}

print("Titres des livres (clés) :", list(bibliotheque.keys()))

print("Valeurs du dictionnaire :", list(bibliotheque.values()))

print("Prix du livre '1984' :", bibliotheque["1984"][2], "DH")

bibliotheque["Les Misérables"] = ("Les Misérables", "Victor Hugo", 200)

bibliotheque["Le Petit Prince"] = ("Le Petit Prince", "Antoine de Saint-Exupéry", 100)

del bibliotheque["L'Étranger"]

print("\n--- Liste des livres et auteurs ---")
for titre, infos in bibliotheque.items():
    print(f"{infos[0]} - {infos[1]}")

print("\n--- Livres dont le prix est supérieur à 100 DH ---")
for titre, infos in bibliotheque.items():
    prix_livre = infos[2]
    if prix_livre > 100:
        print(f"{titre} ({prix_livre} DH)")


biblio = {
    "1984": ("1984", "George Orwell", 150),
    "Le Petit Prince": ("Le Petit Prince", "Antoine de Saint-Exupéry", 100),
    "Les Misérables": ("Les Misérables", "Victor Hugo", 200)
}

def afficher_livres(b):
    print("--- Catalogue de la bibliothèque ---")
    for titre, infos in b.items():
        print(f"Titre : {infos[0]} | Auteur : {infos[1]}")

afficher_livres(biblio)


def ajouter_livre(b, titre, auteur, prix):
    b[titre] = (titre, auteur, prix)
    print(f"Le livre '{titre}' a été ajouté avec succès !")

ajouter_livre(biblio, "L'Alchimiste", "Paulo Coelho", 110)


def chercher_livre(b, titre):
    if titre in b:
        auteur_livre = b[titre][1]
        print(f"Le livre '{titre}' existe. Son auteur est : {auteur_livre}.")
    else:
        print(f"Erreur : Le livre '{titre}' n'est pas dans la bibliothèque.")

chercher_livre(biblio, "1984")
chercher_livre(biblio, "Harry Potter")


def compter_livres(b):
    total = len(b)
    return total

print(f"Nombre total de livres dans la bibliothèque : {compter_livres(biblio)}")























