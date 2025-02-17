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
    """
    Cas de base :
        s=0 : aucun bocal nécessaire, retourne 0
        s<0 : impossible d’atteindre cette quantité -> retourne l'infini
        i=0 : si seul V[0] est dispo 
    Cas général :
        Sans utiliser le bocal V[i] : Appel récursif avec i−1
        En utilisant le bocal V[i] : Réduit s de V[i] et ajoute un bocal
        Retourne le minimum entre ces deux solutions
    """
    if s == 0:
        return 0  # On n'a pas besoin de bocal supplémentaire
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
    """
    But : Calcule m(s,i,V) avec la possibilité d’être interrompu après un certain temps grâce à un signal
    
    Changements par rapport à m(s,i,V) :
        Si stop_event est déclenché, l'exécution s'arrête immédiatement en retournant 0
        Fonction utile pour limiter les boucles récursives qui pourraient être longues
    """
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


def main_threading(S,V,stop_event):
    """
    But : Permet d'exécuter m_threading() en surveillant les erreurs de récursion
    Fonctionnement :
        Essaie d’exécuter m_threading(S, len(V)-1, V, stop_event)
        Si une erreur de récursion survient (RecursionError), affiche un message d’erreur
        Attend que stop_event soit déclenché avant de terminer, pour éviter une boucle infinie
    """
    try:
        m_threading(S, len(V)-1, V,stop_event)
    except RecursionError:
        print("Erreur de recursion")
        while(stop_event.is_set()==False):
            continue
        




