#!/usr/bin/env python3.11

import exemple as ex
from copy import deepcopy
import random
import queue
import time
import matplotlib.pyplot as plt
import func_tas as heap
import numpy as np
import gurobipy as gp
from gurobipy import GRB



def studentpref(file):
    """
    Lit le fichier des préférences des étudiants sur les masters et retourne une matrice CE qui,
    en ligne i, contient le classement des parcours selon les préférences de l’étudiant i
    """
    content = ex.lectureFichier(file)
    cE= [[0]*9 for i in range ((int)(content[0][0]))]
    i=0
    for k in range(1,len(content)):
        w=2
        for j in range (9):
            cE[i][j]=content[k][w]
            w+=1
        i+=1

    return cE


def masterpref(file):
    """
    Lit le fichier des préférences des masters sur les étudiants et retourne une matrice CP qui,
    en ligne i, contient le classement des étudiants selon les préférences du master i
    """
    content = ex.lectureFichier(file)
    cP= [[0]*(int)(content[0][1]) for i in range (9)]
    i=0
    for k in range (2,len(content)):
        w=2
        for j in range((int)(content[0][1])):
            cP[i][j]=content[k][w]
            w+=1
        i+=1

    return cP


    """ question 2
    1. O(1), structure : Queue
    2. O(1), structure : tableau de mise a jour du suivi des demandes
    3. O(1), structure : matrice des positions des etudiants j pour chaque parcours i
    4. O(1), structure : tas(la racine est l'étudiant le - préféré)
    5. O(1.log(n)), structure : Mise a jour du tas en O(log(n))
    """

def capacity_master(file):
    """
    Retourne le tableau des capacités d'un parcours récupéré dans un fichier
    """
    content = ex.lectureFichier(file)
    content[1].remove("Cap")
    return(content[1])

def GS_etu(cE,cP,capacity):
    """
    Initialisation des étudiants et Master commme libre. Pour chaque master, un tas représentant les élèves
    du moins préféré au plus préféré et une liste pour chaque master avec la position dans le master de 
    chaque éleve i
    La recherche des préferences du master se fera dans le tas et on utilisera le tableau de verification en O(1)
    Retourne un dictionnaire {étudiant : valeur} qui contient pour le i-ème étudiant, son parcours assigné
    """
    #Initialisation de la liste des etudiants tous libres au départ O(n)
    list_etu=[i for i in range (len(cE))] 

    #Initialisation matrice des positions des étudiants dans chaque master O(n*m)
    tabPref=[[0]* len(cE) for _ in range(len(cP))]
    for i in range(len(cP)):
        for j in range(len(cP[0])):
            tabPref[i][(int)(cP[i][j])]=(int)(j)

    #Initialisation des tas dans chaque master O(m)
    tas = [[] for _ in range(len(cP))]

    #Dictionnaire d'affectation pour le i-eme étudiant
    affectation={} 

    #Initialisation de la Queue 
    q = queue.Queue(len(list_etu))
    for etu in list_etu:
        q.put((int)(etu))

    #Initialisation du tableau de suivi en O(n)
    suivi=[0 for i in range (len(list_etu))]
    nb_iter=0
    while(not q.empty()):
        etu_courant=q.get()
        while(len(cE[etu_courant])!=0):
            nb_iter+=1
            ask=(int)(cE[etu_courant][suivi[etu_courant]])

            #S'il y a de la place on affecte le premier étudiant de la liste a son i-eme choix 
            if ((int)(capacity[ask])>0):

                heap.put(tas[ask],(int)(tabPref[ask][etu_courant]))
                capacity[ask]=(int)(capacity[ask])-1
                suivi[etu_courant]+=1
                affectation[(int)(etu_courant)]=(int)(ask)
                break
            
            #Sinon on doit comparer le dernier etudiant dans la liste du master (son moins préféré)
            else:
                pos_last_etu=heap.valracine(tas[ask])
                
                last_etu=cP[ask][pos_last_etu]

                #Si le nouvel étudiant a une meilleure position que l'etudiant pris dans le tas alors on le remplace.
                if(tabPref[ask][etu_courant]<pos_last_etu):

                    heap.pop(tas[ask])
                    heap.put(tas[ask],tabPref[ask][etu_courant])

                    # on ajoute dans le tas le nouvel étudiant et on remet l'etudiant déjà choisi dans la liste_etu
                    suivi[etu_courant]+=1
                    affectation[etu_courant]=(int)(ask)
                    del affectation[(int)(last_etu)]
                    q.put((int)(last_etu))
                    break

                else:
                    suivi[etu_courant]+=1
                    continue

    return affectation,nb_iter


def GS_master(cE,cP,capacity):
    """
    Tant qu'il existe un Master libre qui n'a pas proposer a tout les étudiants, il choisis le premier étudiant E
    dans sa liste, si le master n'a pas atteint sa capacite max et que l'étudiant est dans aucun master 
    alors on prend l'etudiant E. Sinon on doit comparer si l'etudiant prefere sont master actuelle ou le master qui propose.
    Si il prefere le master courant on remplace le pire master de l'étudiant par le master courant. Sinon E reste dans son master
    """

    #Initialisation list_master
    list_master=[i for i in range(len(cP))]
    
    #Initialisation matrice des preferences des master pour chaque etudiant
    tabPref=[[0]*len(cP) for _ in range(len(cE))]
    for i in range(len(cE)):
        for j in range(len(cE[0])):
            tabPref[i][(int)(cE[i][j])]=(int)(j)

    #Initialisation d'une liste des master actuelle pour chaque eleve
    eleve_affect = [-1 for _ in range(len(cE))]

    #Tableau d'affectation pour le i-eme master
    affectation={}

    #Initialisation de la Queue 
    is_in=set()
    q = queue.Queue(len(list_master))
    for master in list_master:
        q.put((int)(master))
        is_in.add(master)

    #Initialisation du tableau de suivi
    suivi=[0 for i in range (len(list_master))]
    ancienmaster=-1
    nb_iter=0
    while(not q.empty()):
        master_courant=q.get()
        is_in.remove(master_courant)
        while((int)(capacity[master_courant])>0 and suivi[master_courant]<len(cP[master_courant])):
            nb_iter+=1
            # Si l'eleve n'est affecté à aucun master on l'affecte au master courant et on retire l'eleve des eleve parcouru
            if(eleve_affect[(int)(cP[(int)(master_courant)][suivi[master_courant]])]==-1):

                # l'eleve est affecté au master courant    
                eleve_affect[(int)(cP[master_courant][suivi[master_courant]])]=master_courant 
                affectation[(int)(cP[master_courant][suivi[master_courant]])]=master_courant
                suivi[master_courant]+=1 # on retire l'eleve de la liste des eleves affectés au master
                capacity[master_courant]=(int)(capacity[master_courant])-1

            else:
                # on compare le master de l'etudiant actuel avec le ùaster courant 
                post_actual_master=tabPref[(int)(cP[master_courant][suivi[master_courant]])][master_courant]
                pos_last_master=tabPref[(int)(cP[master_courant][suivi[master_courant]])][eleve_affect[(int)(cP[master_courant][suivi[master_courant]])]]
                ancienmaster=eleve_affect[(int)(cP[master_courant][suivi[master_courant]])]

                if(post_actual_master<pos_last_master):
                    if(not ancienmaster in is_in): 
                        #on remet l'ancien master dans les masters libres
                        q.put(ancienmaster) 
                        is_in.add(ancienmaster)

                    # le master courant est accepté :

                    # l'eleve est affecté au master courant
                    eleve_affect[(int)(cP[master_courant][suivi[master_courant]])]=(int)(master_courant) 
                    # on retire la capacite au master courant
                    capacity[master_courant]=(int)(capacity[master_courant])-1 
                    # on ajoute l'etudiant a la liste d'affectation du master courant 
                    affectation[(int)(cP[master_courant][suivi[master_courant]])]=master_courant 
                    # on remet de la capacite à l'ancien master
                    capacity[ancienmaster]=(int)(capacity[ancienmaster])+1 
                    suivi[master_courant]+=1

                else:
                    # L'etudiant rejette la proposition du master donc on le retire de la liste du master
                    suivi[master_courant]+=1 
    
    return affectation,nb_iter


def paires_instables(prefetu,prefspe,affectes):
    """
    Soit l'étudiant i. Si son parcours préféré disponible j dont la capacité est remplie et dont l'étudiant le moins préféré
    affecté à ce même parcours j, est moins préféré que l'etudiant i, alors (i,j) est une paire instable
    """
    p = [] # tableau de paires instables

    # matrice des positions des etudiants j pour chaque parcours i
    pos = [[-1 for _ in range(len(prefetu))] for _ in range(len(prefspe))]
    for i in range(len(prefspe)):
        for j in range(len(prefetu)):
            pos[i][(int)(prefspe[i][j])] = j

    for specourant in set(affectes.values()): #on parcourt chaque master
        etu_spe=[etu for etu, master in affectes.items() if master == specourant]
        for etu in etu_spe: # on parcourt les etudiants affectes dans le master courant 
            for i in range(len(prefetu[etu])): #on parcourt les masters pref de l'etudiant etucourant
                spepref = (int)(prefetu[etu][i])
                if spepref == specourant: # si etucourant a son master pref alors (etucourant,masterpref) n'est pas une paire instable
                    break  
                
                else: #s'il n'a pas eu son master pref
                    posmax=-1
                    for etulast in [etu for etu, master in affectes.items() if master == spepref]: #etudiant le - préféré pour spepref
                        if(pos[spepref][etulast]>posmax):
                            etucompare=etulast
                            posmax=pos[spepref][etulast]
                    
                    #si spepref préfère etu à etucompare
                    if pos[spepref][etu] < pos[spepref][etucompare]:
                        p.append((etu, spepref))

    return p


def generate_cE(n,nb_parcours):
    """
    Génère une matrice des préférences des n étudiants sur les 9 parcours du master
    """
    cE=[[] for _ in range(n)]
    for i in range(n):
        for j in range(nb_parcours):
            cE[i]=list(range(0,nb_parcours))
            random.shuffle(cE[i])
    return cE

def generate_cP(n,nb_parcours):
    """
    Génère une matrice des préférences des 9 parcours sur les n étudiants
    """
    cP=[[] for _ in range(nb_parcours)]
    for i in range(nb_parcours):
        for j in range(n):
            cP[i]=list(range(0,n))
            random.shuffle(cP[i])
    return cP

def time_gs():
    """
    - Génère des matrices de préférences côté étudiant et côté master pour un nombre d'étudiants n donné
    - Puis génère un tableau de capacités de n places 
    - Appelle l'algorithme de Gale-Shapley des deux côtés en calculant leur temps d'exécution respectif
    - Répète le processus ci-dessus 10 fois avec un n croissant et calcule la moyenne totale
    - Crée un graphique de la variation du temps d'exécution en fonction du nombre d'étudiants
    """
    tests_master = []
    tests_etu = []
    
    for n in range(200,2200,200):
        
        print("n = ",n)
       
        val_master=0
        val_etu=0
        for i in range (10):
            cE = generate_cE(n,9)
            cP = generate_cP(n,9)
            capacites = [random.randint(1, n//2) for _ in range(9)] # capacites entre 1 et n/2 pour equité
            while sum(capacites) != n:
                diff = n-sum(capacites)
                if diff > 0: # on met diff dans une capacite random
                    capacites[random.randint(0, 8)] += diff
                if diff < 0: #si sum(capacites) > n
                    # on ajt diff(negatif) à une capacite random
                    ind = random.randint(0, 8)
                    capacites[ind] = max(1, capacites[ind] + diff) # max entre 1 pourr eviter des capacités negatives
                                                    
                                                            
            capacites2=[val for val in capacites]   # car les fonctions GS modifient directement le tableau initial
            debut = time.time()
            affectes_master = GS_master(cE,cP, capacites)
            fin = time.time()
            val_master+=(fin-debut)
            debut = time.time()
            affectes_etu = GS_etu(cE,cP, capacites2)
            fin = time.time()
            val_etu+=(fin-debut)
        val_etu=val_etu/10
        val_master=val_master/10
        # print("coté master : ", val_master)
        # print("coté etu : ", val_etu)
        tests_master.append(val_master)
        tests_etu.append(val_etu)
        # print("coté etu : ", fin-debut)
        # print("Liste des paires instable côté etu :",paires_instables(cE,cP,affectes_etu))
        # print("Liste des paires instable côté master :",paires_instables(cE,cP,affectes_master))



    # print("\n")
    # print("moyenne temps parcours = ", sum(tests_master) / len(tests_master)," secondes")
    # print("moyenne temps etu = ", sum(tests_etu) / len(tests_etu)," secondes")
    
    val_n = [n for n in range(200, 2200, 200)]
    # 1. Graphique avec sqrt
    plt.figure(figsize=(8, 5))
    plt.plot(val_n, np.sqrt(tests_etu), label="Temps_etu (racine)", color="blue")
    plt.plot(val_n, np.sqrt(tests_master), label="Temps_master (racine)", color="red")
    plt.xlabel("n")
    plt.ylabel("Temps d'execution (s)")
    plt.title("Graphique des temps d'execution de Gale-Shapley (racine)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

    # 2. Graphique avec log
    plt.figure(figsize=(8, 5))
    plt.plot(val_n, np.log(tests_etu), label="Temps_etu (log)", color="blue")
    plt.plot(val_n, np.log(tests_master), label="Temps_master (log)", color="red")
    plt.xlabel("n")
    plt.ylabel("Temps d'execution (s) (log)")
    plt.title("Graphique des temps d'execution de Gale-Shapley (log)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

    # 3. Graphique avec les valeurs normales
    plt.figure(figsize=(8, 5))
    plt.plot(val_n, tests_etu, label="Temps_etu", color="blue")
    plt.plot(val_n, tests_master, label="Temps_master", color="red")
    plt.xlabel("n")
    plt.ylabel("Temps d'execution (s)")
    plt.title("Graphique des temps d'execution de Gale-Shapley (Valeurs Normales)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()
    return val_n,tests_etu,tests_master
    

def it_gs():
    """
    - Génère des matrices de préférences côté étudiant et côté master pour un nombre d'étudiants n donné
    - Puis génère un tableau de capacités de n places 
    - Appelle l'algorithme de Gale-Shapley des deux côtés en calculant leur temps d'exécution respectif
    - Répète le processus ci-dessus 10 fois avec un n croissant et calcule la moyenne totale
    - Crée un graphique de la variation du nombre d'iteration en fonction du nombre d'étudiants
    """

    tests_master = []
    tests_etu = []
    
    for n in range(200,2200,200):
        
        print("n = ",n)
       
        val_master=0
        val_etu=0
        for i in range (10):
            cE = generate_cE(n,9)
            cP = generate_cP(n,9)
            capacites = [random.randint(1, n//2) for _ in range(9)] # capacites entre 1 et n/2 pour equité
            while sum(capacites) != n:
                diff = n-sum(capacites)
                if diff > 0: # on met diff dans une capacite random
                    capacites[random.randint(0, 8)] += diff
                if diff < 0: #si sum(capacites) > n
                    # on ajt diff(negatif) à une capacite random
                    ind = random.randint(0, 8)
                    capacites[ind] = max(1, capacites[ind] + diff) # max entre 1 pourr eviter des capacités negatives



            capacites2=[val for val in capacites]   # car les fonctions GS modifient directement le tableau initial
            affectes_master,nb_itemaster = GS_master(cE,cP, capacites)
            
            val_master+=(nb_itemaster)
            affectes_etu,nb_iteetu = GS_etu(cE,cP, capacites2)
            val_etu+=(nb_iteetu)
        val_etu=val_etu/10
        val_master=val_master/10
        print("coté master : ", val_master)
        print("coté etu : ", val_etu)
        tests_master.append(val_master)
        tests_etu.append(val_etu)


    # print("\n")
    # print("moyenne nb_ite parcours = ", sum(tests_master) / len(tests_master)," secondes")
    # print("moyenne nb_ite etu = ", sum(tests_etu) / len(tests_etu)," secondes")
    

    val_n=[n  for n in range(200,2200,200)]
    plt.figure(figsize=(8,5))

    plt.plot(val_n,tests_etu,label="ite_etu",color="blue")
    plt.plot(val_n,tests_master,label="ite_master",color="red")
    plt.xlabel("n")
    plt.ylabel("Nombre d'iteration")
    plt.title("Graphique des nombre d'iterations de Gale-Shapley")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()
    return val_n,tests_etu,tests_master

def analyse_sol(affectations,borda_etu,borda_parcours):
    """Renvoie la liste des paires instable,l'utilite en moyenne, et l'utilite minimale pour une affectations."""
    stable=paires_instables(studentpref("PrefEtu.txt"),masterpref("PrefSpe.txt"),affectations)

    total_uti_etu=0
    total_uti_parcours=0
    list_uti_etu=[]
    for etu,parcours in affectations.items():
        total_uti_etu+=borda_etu[etu][parcours] 
        total_uti_parcours+=borda_parcours[parcours][etu]
        list_uti_etu.append(borda_etu[etu][parcours])

    total_uti=total_uti_etu+total_uti_parcours #Calculer la somme totale des utilités

    utilite_moyenne=total_uti/len(borda_etu) #Utilite moyenne

    utilite_minimale=min(list_uti_etu) #Utilite minimale

    return stable,utilite_moyenne,utilite_minimale

