def tri(tab):
    #i est le premier indice de la zone non triee, j le dernier indice.
    #Au debut, la zone non triee est le tableau entier.
    i= 0 #premier terme de tab on rajoute +1
    j= len(tab) -1 #dernier terme on rajoute -1 jusqua que i et j se rencontrent
    while i != j :
        if tab[i]== 0: # si tab[i] = 0 on rajoute 1
            i= i+1
        else :
            valeur = tab[j] #?
            tab[j] = tab[i] #?
            tab[i]= valeur #?
            j= j-1
    return tab