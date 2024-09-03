#DEMINEUR TME 5-S1

from enum import Enum
class Status(Enum):
    COVERED = 1
    UNCOVERED = 2
    MARK = 3

def init_plateau(taille, val): #ex1q1
    tab=taille*[val]
    for i in range(0,taille):
        tab[i]=taille*[val]
    return tab

def init_mine(tab,nbmines): #ex1q2
    ens_coo=[]
    while(nbmines!=0):
        i= randint(0,len(tab))
        j= randint(0,len(tab))
        tab[i][j]=9
        ens_coo.append((i,j))
        nbmines+=1

def liste_voisins(x,y,taille): #ex1q3
    liste=[]
    ax=x-1
    ay=y-1
    bx=x+1
    by=y+1
    if ax>=0:
        liste.append((ax,y))
        if ay>=0:
            liste.append((ax,ay))
        if by<=taille:
            liste.append((ax,by))
    if bx<=taille:
        liste.append((bx,y))
        if ay>=0:
            liste.append((bx,ay))
        if by<=taille:
            liste.append((bx,by))
    if by<=taille:
        liste.append((x,by))
    if ay>=0:
        liste.append((x,ay))

    return liste

def init_compte(tab, liste): #ex1q4
    for i in range(0,len(tab)):
        for j in range(0,len(tab)):
            cpt=0
            liste=liste_voisins(i,j,len(tab))
            for k in liste:
                if(liste[k]==9):
                    tab[i][j]+=1
    return tab

def init_plateau_mines(taille,nbmines): #ex1q5
    tab=init_plateau(taille,0)
    init_mine(tab,nbmines)
    for i in tab:
        for j in tab:
            if tab[i][j] == 9:
                init_compte(tab,voisin_mine)
    return tab

def affichetab(tab,taille): #ex1q6
    for i in range(0,taille):
        for j in range(0,taille):
            print(tab[i][j])


def plateau_status(tab): #ex2q3
   ps = [[Status.COVERED for j in range(len(tab))] for i in range(len(tab))]
   return ps

def decouvre_case(i,j,plateau,ps): #ex3q1
    if ps[i][j]==Status.COVERED:
        ps[i][j] = Status.UNCOVERED
        if plateau[i][j]==9:
            return False
    return True

def mark_case(i,j,plateau,ps): #ex3q2
    if ps[i][j] == Status.COVERED:
        ps[i][j]= Status.MARK
    elif ps[i][j] == Status.MARK:
        ps[i][j]= Status.COVERED
    return ps

def mine_mark(i,j,plateau, ps): #ex3q3
    nb_mines_voisines += 1
    voisin=liste_voisins(i,j,len(plateau))
    for x in voisin:
        for y in voisin:
            if ps[x][y] == Status.MARK:
                nb_mines_voisines += 1

    if nb_mines_voisines == plateau[x][y]:
        for vx in voisin:
            for vy in voisin:
                if decouvre_case(vx,vy,plateau,ps) == False:
                    return False
    return True

def jeu(): #ex4
    nbmines= input(int("Entrez un nombre de mines"))
    taille= input(int("Entrez une taille"))
    plateau= init_plateau(taille,9)
    init_mine(plateau,nbmines)
    liste=[]
    init_compte(plateau,liste)
    init_plateau_mines(taille,nbmines)
    ps=plateau_status(plateau)
    cx,cy = coordonnee
    while plateau[cx][cy] != 9 & nbmines!=0:
        cx=input(int("Entrez la coordonnée x"))
        cy=input(int("Entrez la coordonnée y"))
        mine_mark(cx,cy,plateau,ps)
        nbmines-=1
        affichetab(plateau,taille)
    if nbmines==0:
        print("GG")
    else:
        print("PERDU")