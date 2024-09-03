def occurences_lettres(phrase):
    dico={}
    for i in phrase:
        if i in dico:
            dico[i] +=1
        else:
            dico[i] =1
    return dico