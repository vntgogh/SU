def init_plateau(n: int,val: int)->list: #question1
    '''initialisation du tableau'''
    tab=[]
    for i in range(0,n):
        l=[]
        for j in range(0,n):
              l.append(val)
        tab.append(l)
    print(init_plateau(8,0))

assert init_plateau(8,0)==[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
assert init_plateau(2,9)==[[9, 9], [9, 9]]
assert init_plateau(5,5)==[[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]


def init_mine(plateau_mines: list, nb_mines : int) -> list: #question2
    for ligne in range(0,8):
        lstligne = []
        for colonne in range(0,8):
            if random.randint(1,64) ==9:
                lstligne.append(1)
            else:
                lstligne.append(0)
        plateau_mines.append(lstligne)
    print(init_mine(plateau_mines))


def liste_voisins(caseadj : list,n: int) -> list: #question3
    x=ligne
    y=colonne
    while x< taille and y <taille:
        if case[val] == 9:
            print("Perdu")
    else:
        while case == tab[x][y]:
            if (y =! 0 and x =!0) and (caseadj= tab[x][y-1]) or (caseadj= tab[x-1][y]):
            if caseadj= tab[x][y+1]:
            if caseadj= tab[x+1][y]:
            if caseadj= tab[x-1][y-1]:
            if caseadj= tab[x+1][y+1]:
            if caseadj= tab[x-1][y+1]:
            if caseadj= tab[x+1][y-1]

