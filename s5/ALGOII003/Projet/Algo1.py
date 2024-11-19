import math
import time
def read():
    with open("data.txt", "r") as fichier:
        contenu = fichier.read().split()
        S = int(contenu[0])
        K = int(contenu[1])
        V = [int(val) for val in contenu[2:]]
    return S, K, V

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


def main():
    S, K, V = read()
    m(S,len(V)-1,V)

def main_threading(stop_event):
    S, K, V = read()
    try:
        m_threading(S, len(V)-1, V,stop_event)
    except RecursionError:
        print("Erreur de recursion")
        while(stop_event.is_set()==False):
            continue
        