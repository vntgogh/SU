import random
import re
import argparse

class Demineur_case:
    def init_mine(self):
        self.valeur = 0
        self.mine = False
        self.decouverte = False

    def get_valeur(self):
        return self.valeur

    def get_mine(self):
        return self.mine

    def get_decouverte(self):
        return self.decouverte

    def set_valeur(self, valeur):
        self.valeur = valeur

    def set_mine(self, mine):
        self.mine = mine

    def set_decouverte(self, decouverte):
        self.decouverte= decouverte

    def __str__(self):
        return str(self.valeur)


class Demineur_grille:
    def init_mine(self, taille, nb_mines):
        self.taille = taille
        self.nb_mines = nb_mines
        self.plateau = [[Demineur_case() for i in range(taille)] for k in range(taille)]
        self.case_jouables = taille * taille - nb_mines
        compteur_mines = 0
        while compteur_mines < nb_mines:
            x= random.randint(0, self.taille-1)
            y= random.randint(0, self.taille-1)
            if not self.plateau[x][y].get_mine(0):
                compteur_mines +=1
                self.place_mine(x,y)

    def get_cases_jouables(self):
        return self.cases_jouables

#ex1 question5
    def init_plateau_mine(self, x, y):
        self.plateau[x][y].set_mine(True)
        for k in range(x-1,x+2):
            for i in range(y-1,y+2):
                if k >=0 and i >=0 and k < self.taille and i < self.taille:
                    self.plateau[k][i].set_valeur(self.plateau[k][i].get_valeur()+1)

    def __str__(self):
        grille = ' '
        for k in range(self.taille):
            if k <10:
                grille += ' ' *2 +str(k)+ ' '*2
            else:
                grille += ' ' *2 + str(k)+ ' '*2

        grille += "\n"
        for k in range(self.taille):
            grille += '-'*5
            if k == self.taille-1:
                grille+= '--' + "\n"
        for k in range(self.taille):
            if k<10:
                grille += str(k)+' '
            else:
                grille += str(k)+' '
            for i in range(self.taille):
                if self.plateau[k][i].get_decouverte():
                    if self.plateau[k][i].get_mine():
                        grille += "*  "
                    else:
                        grille += str(self.plateau[k][i].get_valeur()) + '  '
                else:
                    grille += '   '
            grille += "\n"
        for k in range(self.taille):
            grille += '-'*5
            if k == self.taille-1:
                 grille += '--' + "\n"
        return grille

#ex3 question3
    def decouverte_case(self,x,y):
        self.cases_jouables = self.cases_jouables-1
        self.plateau[x][y].set_decouverte(True)
        if self.plateau[x][y].get_mine():
            return False
        else:
            if self.plateau[x][y].get_valeur() == 0:
                for k in range(x-1,x+2):
                    for i in range(y-1,y+2):
                        if (k >=0 and i >=0 and
                                k < self.taille and
                                i < self.taille and
                                not (k==x and i == y) and
                                not self.plateau[k][i].get_decouverte()):
                            self.decouverte_case(k,i)
                return True
            else:
                return True

class Demineur_jeu:
    def __init__(self,taille,mine):
        self.taille = taille
        self.mine = mine
        self.grille = Demineur_grille(taille,mine)
        self.victoire = False
        self.defaite = False

    def demande_joueur(self):
        saisie_valide = False
        while not saisie_valide:
            saisie_valide = True
            saisie = input("Où souhaitez-vous jouer? Entrez ligne, colonne : ")
            saisie_analyse = re.match(r"^\s*(?P<x>\d+)\s*,\s*(?P<y>\d+)\s*$", saisie)
            if saisie_analyse :
                x = int(saisie_analyse.group("x"))
                y = int(saisie_analyse.group("y"))
                if x>= self.taille:
                    print("x trop grand")
                    saisie_valide = False
                if y >= self.taille:
                    print("y trop grand")
                    saisie_valide = False
                if selfgrille.plateau[x][y].get_decouverte() == True:
                    print("Case déjà découverte")
                    saisie_valide = False
            else:
                print("Les coordonnées ne sont pas conformes.")
                saisie_valide = False
        return x, y

    def lancer_jeu(self):
        while not (self.victoire or self.defaite):
            print(self.grille)
            x, y = self.demande_joueur()
            self.defaite = not self.grille.decouverte_case(x,y)
            if self.grille.cases_jouables == 0:
                self.victoire = True
        if self.defaite:
            print('Game over')
        if self.victoire:
            print('Vous avez découvert toutes les mines')
        for k in range(0, self.taille):
            for i in range(0, self.taille):
                self.grille.plateau[k][i].set_decouverte(True) #ex2question3
        print(self.grille)

