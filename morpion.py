class tictoe:
    def __init__(self):
        self.plateau = [[" " for _ in range(4)] for _ in range(4)]
        self.joueur_actuel = "X"

    def afficher_plateau(self):
        for ligne in self.plateau:
            print("|" + "|".join(ligne) + "|")
            print("-------------")
    
    def verifier_victoire(self, joueur):
        lignes = any(all(cell == joueur for cell in ligne) for ligne in self.plateau)
        colonnes = any(all(ligne[i] == joueur for ligne in self.plateau) for i in range(4))
        diagonale1 = all(self.plateau[i][i] == joueur for i in range(4))
        diagonale2 = all(self.plateau[i][3 - i] == joueur for i in range(4))
        
        return lignes or colonnes or diagonale1 or diagonale2
    
    def coup_valide(self, x, y):
        return self.plateau[y][x] == " "
    
    def jouer_coup(self, x, y, joueur):
        self.plateau[y][x] = joueur

    def coups_possibles(self):
        return [(x, y) for x in range(4) for y in range(4) if self.plateau[y][x] == " "]

    def minimax(self, maximisant, joueur, profondeur=0):
        if self.verifier_victoire("X"):
            return -1, None
        elif self.verifier_victoire("O"):
            return 1, None
        elif not self.coups_possibles():
            return 0, None

        if maximisant:
            meilleur_score = float("-inf")
            meilleur_coup = None
            for x, y in self.coups_possibles():
                self.jouer_coup(x, y, joueur)
                score, _ = self.minimax(False, "X", profondeur + 1)
                self.jouer_coup(x, y, " ")
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_coup = (x, y)
            return meilleur_score, meilleur_coup
        else:
            meilleur_score = float("inf")
            meilleur_coup = None
            for x, y in self.coups_possibles():
                self.jouer_coup(x, y, joueur)
                score, _ = self.minimax(True, "O", profondeur + 1)
                self.jouer_coup(x, y, " ")
                if score < meilleur_score:
                    meilleur_score = score
                    meilleur_coup = (x, y)
            return meilleur_score, meilleur_coup

    def jouer(self):
        self.afficher_plateau()
        while True:
            if self.joueur_actuel == "X":
                x, y = map(int, input("Entrez les coordonnées (x y) : ").split())
                if self.coup_valide(x, y):
                    self.jouer_coup(x, y, "X")
                    if self.verifier_victoire("X"):
                        print("X gagne!")
                        break
                    self.joueur_actuel = "O"
                else:
                    print("Coup invalide.")
            else:
                print("Tour de l'IA...")
                _, coup = self.minimax(True, "O")
                if coup:
                    self.jouer_coup(coup[0], coup[1], "O")
                    self.afficher_plateau()
                    if self.verifier_victoire("O"):
                        print("O gagne!")
                        break
                    self.joueur_actuel = "X"
                else:
                    print("Match nul!")
                    break
            self.afficher_plateau()

if __name__ == "__main__":
    jeu = tictoe()
    jeu.jouer()
