import random

PENDU_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

print()
print("Bienvenue dans le Hangman Game :")
print()
print("1 : facile")
print("2 : moyen")
print("3 : difficile")
print()

niveau = ""
while niveau not in ["1", "2", "3"]:
    niveau = input("Choisissez un niveau : ").strip()
    if niveau not in ["1", "2", "3"]:
        print("Niveau invalide. Veuillez entrer 1, 2 ou 3.")

niveaux_noms = {
    "1": "Facile",
    "2": "Moyen",
    "3": "Difficile"
}

fichiers_niveaux = {
    "1": "words_list/mots_faciles.txt",
    "2": "words_list/mots_moyens.txt",
    "3": "words_list/mots_difficiles.txt"
}

nom_fichier = fichiers_niveaux[niveau]

with open(nom_fichier, "r", encoding="utf-8") as f:
    mots = [ligne.strip().lower() for ligne in f if ligne.strip()]

mot_a_deviner = random.choice(mots)
lettres_trouvees = ["_" for _ in mot_a_deviner]
lettres_essayees = set()
chances = 6

print()
print(f"Niveau sélectionné : {niveaux_noms[niveau]}")

while chances > 0 and "_" in lettres_trouvees:
    print(PENDU_PICS[6 - chances])
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


print(PENDU_PICS[6 - chances])
if "_" not in lettres_trouvees:
    print("\n🎉 Félicitations ! Vous avez deviné le mot :", mot_a_deviner)
else:
    print("\n💀 Vous avez perdu. Le mot était :", mot_a_deviner)