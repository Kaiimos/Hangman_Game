import random

mots = ["python", "programmation", "ordinateur", "intelligence"]

mot_a_deviner = random.choice(mots)
lettres_trouvees = ["_" for _ in mot_a_deviner]
lettres_essayees = set()
chances = 6

print("Bienvenue dans le jeu du Pendu !")

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

if "_" not in lettres_trouvees:
    print("\nFélicitations ! Vous avez deviné le mot :", mot_a_deviner)
else:
    print("\nVous avez perdu. Le mot était :", mot_a_deviner)

