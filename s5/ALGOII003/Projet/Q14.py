import math
import random
import Algo2_v3 as A2
import Algo3 as A3


def TGC(k,V):#Fournie
    #vérifie si un système de capacités est glouton-compatible
    S=0
    j=1
    if k>=3:
        for S in range(V[3]+2,V[k-1]+V[k]-1):
            for j in range(k):
                if(V[j]<S) and (A3.AlgoGlouton2(S,k,V)>1+A3.AlgoGlouton2(S-V[j],k,V)):
                    return False
    return True

def sc_random(k,pmax):
    """Génère un système aléatoire de capacités.

    - k : Nombre de types de bocaux
    - pmax : Capacité maximale
    """
    V = [0 for _ in range(k)]  # Initialisation des capacités
    rtab = [0 for _ in range(k - 1)]  # Temporaire pour générer les valeurs
    V[0] = 1  # Le système doit contenir la capacité 1 (condition essentielle)

    for i in range(k - 1):
        var = random.randint(2, pmax)  # Génération aléatoire entre 2 et `pmax`
        while rtab.__contains__(var):  # Vérifie les doublons
            var = random.randint(2, pmax)
        rtab[i] = var

    rtab.sort()  # Trie les valeurs
    for i in range(1, k):# Remplissage de `V` avec les valeurs triées
        V[i] = rtab[i - 1]  
    return V



#V[1] 0 pmax/k
#V[2] pmax/k * i -1 pmax/4 * i

def proportion_GloutonCompatible(k):
    nb_GC=0 # Compteur de systèmes glouton-compatibles
    for i in range(1,k,1):
        if(TGC(i-1,sc_random(i,40))): # Test de compatibilité
            nb_GC+=1
    return (nb_GC/k)*100 # Calcul en pourcentage

def resolution(f,pmax):
    """Évalue Algo2 et Algo3 pour des systèmes glouton-compatibles et non compatibles
    
    Arguments :
    - f : Facteur d'échelle pour les valeurs de S (plage des tests entre pmax et f * pmax).
    - pmax : Capacité maximale utilisée pour générer les systèmes

    Sauvegarde :
    - Les statistiques sur les systèmes et les écarts dans 'eval_glouton_compatible.txt'.
    """
    nb_GC=0 # Compteur de systèmes compatibles
    nb_NGC=0 # Compteur de systèmes non compatibles
    with open("eval_glouton_compatible.txt","w") as fichier:
        fichier.write("f = "+(str)(f)+"\npmax = "+(str)(pmax)+"\n")
        fichier.write("V Pire_Ecart Ecart_Moyen\n")

    for i in range(10,30,1):
        pire_ecart=0 # Le pire écart entre les solutions gloutonne et optimale
        ecart_moyen=0 # La somme des écarts
        nb_ecart=0 # Nombre total de tests

        V=sc_random(i*2,pmax)  # Génère un système aléatoire
        print(V)

        if(TGC(i,V)):# Test de glouton-compatibilité
            print("glouton compatible")
            nb_GC+=1
        else:
            print("non compatible")
            nb_NGC+=1
            for j in range(pmax,pmax*f,1): # On fait varier S dans [pmax,pmax*f]
                res_A2=A2.backward2(j,i,V) # Solution optimale
                res_A3=A3.AlgoGlouton2(j,i,V) # Solution gloutonne
                #print(res_A2,res_A3)

                if(abs(res_A2-res_A3)>=pire_ecart):
                    pire_ecart=abs(res_A2-res_A3) # Met à jour le pire écart

                ecart_moyen+=abs(res_A2-res_A3) # Cumule les écarts
                nb_ecart+=1

            with open("eval_glouton_compatible.txt","a") as fichier:
                fichier.write("Systeme non glouton compatible : "+(str)(nb_NGC)+"\n")
                fichier.write("[")
                fichier.writelines(f"{v}," for v in V)
                fichier.write("]\n")
                fichier.write("Pire ecart = "+(str)(pire_ecart)+"\n")
                fichier.write("Ecart Moyen = "+(str)(ecart_moyen/nb_ecart)+"\n")


resolution(15,200)