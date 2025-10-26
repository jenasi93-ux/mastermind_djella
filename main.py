import random

def mastermind_creation():
    couleurs = ['Bleu', 'Vert', 'Jaune', 'Rouge', 'Blanc', 'Noir']
    combinaison = []
    for i in range(4):
        couleur = random.choice(couleurs)
        combinaison.append(couleur)
    return combinaison

def jeu_mastermind():
    secret = mastermind_creation()
    print("La combinaison secrète a été générée !")
    print("Tu dois deviner les 4 couleurs dans le bon ordre.")
    print("Couleurs possibles : Bleu, Vert, Jaune, Rouge, Blanc, Noir")

    essais = 1
    while essais <= 10:
        print("\nEssai numéro :", essais)
        entree = input("Tape 4 couleurs séparées par un espace : ")
        choix = entree.split(" ")

        if len(choix) != 4:
            print("Tu dois mettre exactement 4 couleurs !")
            continue

        bien = 0
        mal = 0

        for i in range(4):
            if choix[i] == secret[i]:
                bien += 1
            elif choix[i] in secret:
                mal += 1

        print("Bien placés :", bien)
        print("Mal placés :", mal)

        if bien == 4:
            print("Bravo ! Tu as trouvé la combinaison !")
            break

        essais += 1

    if essais > 10 and bien != 4:
        print("\nDommage, tu n'as plus d'essais.")
        print("La combinaison était :", secret)

jeu_mastermind()
