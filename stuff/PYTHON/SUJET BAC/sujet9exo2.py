def est_parfait(mot) :
    #mot est une chaÃ®ne de caractÃ¨res (en lettres majuscules)
    code_c = ""
    code_a = 0
    for c in mot :
        code_c = code_c + str(dico[c]) #str transforme les lettres en chiffres
        code_a = code_a + dico[c]
    code_c = int(code_c)
    if code_c%code_a ==0 :
        mot_est_parfait = True
    else :
        mot_est_parfait = False
    return [code_a, code_c, mot_est_parfait]
