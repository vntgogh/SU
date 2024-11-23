import math
import time

""""read() - Lis les données dans le fichier data.txt et les retournes."""
def read():
    with open("data.txt", "r") as fichier:
        contenu = fichier.read().split()
        S = int(contenu[0])
        K = int(contenu[1])
        V = [int(val) for val in contenu[2:]]
    return S, K, V

"""m(s,i,V) - Retourne le nombre de bocaux minimaux a utlisé dans V de taille i pour atteindre la quantité s ."""
def m(s, i, V):
    if s == 0:
        return 0  # On n'a pas besoin de bocal supplémentaires
    elif s < 0:
        return math.inf  # Cas impossible
    elif i==0:  # Aucun élément utilisable
        if(s % V[0] == 0):
            return(m(s - V[i],i,V)+1)
        else:
            return math.inf
    else:
        # Calculer la solution minimale avec ou sans le bocal courant
        sans_bocal = m(s, i - 1, V)
        avec_bocal = m(s - V[i], i, V) + 1
        return min(sans_bocal, avec_bocal)

"""m_threading(s, i, V,stop_event) - Cf. m(s,i,v) dans un thread qui est arrete au bout de 60 seconde lorsque stop_event va valoir true"""
def m_threading(s, i, V,stop_event):
    if(stop_event.is_set()):
        #print("fin du programme a i = "+(str)(i))
        return 0
    if s == 0:
        return 0  # On n'a pas besoin de bocal supplémentaires
    elif s < 0:
        return math.inf  # Cas impossible
    elif i==0:  # Aucun élément utilisable
        if(s % V[0] == 0):
            return(m_threading(s - V[i],i,V,stop_event)+1)
        else:
            return math.inf
    else:
        # Calculer la solution minimale avec ou sans le bocal courant
        sans_bocal = m_threading(s, i - 1, V,stop_event)
        avec_bocal = m_threading(s - V[i], i, V,stop_event) + 1
        return min(sans_bocal, avec_bocal)

"""main_lecture() - fonction main qui lis les donnée du data.txt et afficher le resultat de m"""
def main_lecture():
    S, K, V = read()
    print(m(S,len(V)-1,V))

"""main_threading(S,V,stop_event) - lance la fonction m_threading, si la fonction renvoie une exception error, la catch et attend que stop_event soit set a true"""
def main_threading(S,V,stop_event):
    try:
        m_threading(S, len(V)-1, V,stop_event)
    except RecursionError:
        print("Erreur de recursion")
        while(stop_event.is_set()==False):
            continue
        




