import random

print("Bienvenue dans le jeu du Pendu !")

# Menu avec sélection par chiffre
print("\nChoisissez un niveau :")
print("1 - Facile")
print("2 - Moyen")
print("3 - Difficile")

choix = input("Entrez le numéro du niveau (1, 2 ou 3) : ").strip()

# Chemins mis à jour avec le dossier "words_list/"
fichiers_niveaux = {
    "1": "words_list/mots_faciles.txt",
    "2": "words_list/mots_moyens.txt",
    "3": "words_list/mots_difficiles.txt"
}

# Fichier choisi selon l’entrée, défaut = facile
nom_fichier = fichiers_niveaux.get(choix, "words_list/mots_faciles.txt")

# Chargement des mots
try:
    with open(nom_fichier, "r", encoding="utf-8") as f:
        mots = [ligne.strip() for ligne in f if ligne.strip()]
except FileNotFoundError:
    print(f"Erreur : le fichier {nom_fichier} est introuvable.")
    exit()

mot_a_deviner = random.choice(mots).lower()

lettres_trouvees = ["_" for _ in mot_a_deviner]
lettres_essayees = set()
chances = 6

# Boucle principale du jeu
while chances > 0 and "_" in lettres_trouvees:
    print("\nMot à deviner :", " ".join(lettres_trouvees))
    print("Lettres essayées :", " ".join(sorted(lettres_essayees)))
    print(f"Chances restantes : {chances}")
    lettre = input("Devinez une lettre : ").lower()

    if not lettre.isalpha() or len(lettre) != 1:
        print("Veuillez entrer une seule lettre.")
        continue

    if lettre in lettres_essayees:
        print("Vous avez déjà essayé cette lettre.")
        continue

    lettres_essayees.add(lettre)

    if lettre in mot_a_deviner:
        for i, l in enumerate(mot_a_deviner):
            if l == lettre:
                lettres_trouvees[i] = lettre
        print("Bonne réponse !")
    else:
        chances -= 1
        print("Mauvaise réponse.")

# Fin du jeu
if "_" not in lettres_trouvees:
    print("\nFélicitations ! Vous avez deviné le mot :", mot_a_deviner)
else:
    print("\nVous avez perdu. Le mot était :", mot_a_deviner)

