def recherche(tab,couples):
    l=[]
    for i in range(len(tab)-1):
        if tab[i]==tab[i+1]-1:
            l.append((tab[i],tab[i+1]))
    return l