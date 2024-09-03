def rendu(somme_a_rendre):
    nbr=[0,0,0] # n1 n2 et n3
    pieces=[5,2,1]
    for i in range(len(pieces)):
        while somme_a_rendre >= pieces[i]:
            somme_a_rendre = somme_a_rendre - pieces[i]
            nbr[i] = nbr[i] + 1
    return nbr