def moyenne(tab):
    somme = 0
    n= len(tab)
    if tab!= None:
        for i in tab:
            somme+=i
    else:
        return 'erreur'
    return somme / n