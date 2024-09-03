def recherche(caractere,mot):
    compteur=0
    for i in mot:
        if i== caractere:
            compteur+=1
    return compteur
