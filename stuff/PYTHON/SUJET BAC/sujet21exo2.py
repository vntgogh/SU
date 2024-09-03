def dichotomie(tab, x):
    """
        tab : tableau dâ€™entiers triÃ© dans lâ€™ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """

    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin)//2 # dichotomie
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m-1
    return tab,x