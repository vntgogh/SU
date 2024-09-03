def moyenne(liste):
    somme=0
    coef=0
    for i in liste:
        somme+= i[0]*i[1]
        coef+=i[1]
    return somme/coef

