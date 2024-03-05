import random

def afficher_tableau(tableau):
    for ligne in tableau:
        print("|".join(ligne))
        print("-" * 5)

def verifier_gagnant(tableau, joueur):
    gagne = any(all(cellule == joueur for cellule in ligne) for ligne in tableau)
    gagne |= any(all(ligne[i] == joueur for ligne in tableau) for i in range(3))
    gagne |= all(tableau[i][i] == joueur for i in range(3))
    gagne |= all(tableau[i][2 - i] == joueur for i in range(3))
    return gagne

def obtenir_coups_possibles(tableau):
    return [(l, c) for l in range(3) for c in range(3) if tableau[l][c] == " "]

def jouer_coup(tableau, coup, joueur):
    l, c = coup
    tableau[l][c] = joueur

def ia_coup(tableau, joueur):
    for coup in obtenir_coups_possibles(tableau):
        jouer_coup(tableau, coup, joueur)
        if verifier_gagnant(tableau, joueur):
            return coup
        tableau[coup[0]][coup[1]] = " "
    for coup in obtenir_coups_possibles(tableau):
        jouer_coup(tableau, coup, "X" if joueur == "O" else "O")
        if verifier_gagnant(tableau, "X" if joueur == "O" else "O"):
            return coup
        tableau[coup[0]][coup[1]] = " "
    return random.choice(obtenir_coups_possibles(tableau))

def jeu():
    tableau = [[" " for _ in range(3)] for _ in range(3)]
    joueur_actuel = "X"

    while True:
        afficher_tableau(tableau)
        if joueur_actuel == "X":
            ligne = int(input("Entrez votre ligne: "))
            colonne = int(input("Entrez votre colonne: "))
            coup = (ligne, colonne)
            if coup in obtenir_coups_possibles(tableau):
                jouer_coup(tableau, coup, joueur_actuel)
            else:
                print("Coup invalide.")
                continue
        else:
            coup = ia_coup(tableau, joueur_actuel)
            jouer_coup(tableau, coup, joueur_actuel)
            print(f"L'IA ({joueur_actuel}) a jouÃ©.")

        if verifier_gagnant(tableau, joueur_actuel):
            afficher_tableau(tableau)
            print(f"Le joueur {joueur_actuel} gagne!")
            break
        if not obtenir_coups_possibles(tableau):
            afficher_tableau(tableau)
            print("Match nul!")
            break
        joueur_actuel = "O" if joueur_actuel == "X" else "X"

if __name__ == "__main__":
    jeu()
