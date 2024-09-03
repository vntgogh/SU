def recherche(tab,n):
    tab=[]
    for i in tab:
        if n == tab[i]:
            return i
        else:
            return -1
