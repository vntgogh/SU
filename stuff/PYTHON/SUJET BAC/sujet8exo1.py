def recherche(elt,tab):
    indice = 0
    for v in tab:
        if v == elt:
            return indice
        if v!= elt:
            indice = indice + 1
        else:
            return -1