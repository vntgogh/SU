import exemple as ex
from copy import deepcopy
import random
import queue
import time
import matplotlib.pyplot as plt
import func_tas as heap


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

        question 3
    coté etu : O(n*m*log(n))
    coté mster : O(n*m)
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
    #Initialisation de la liste des etudiants tous libres au départ
    list_etu=[i for i in range (len(cE))]

    #Initialisation matrice des positions des étudiants dans chaque master
    tabPref=deepcopy(cP)
    for i in range(len(cP)):
        for j in range(len(cP[0])):
            tabPref[i][(int)(cP[i][j])]=(int)(j)

    #Initialisation des tas dans chaque master
    tas = [[] for _ in range(len(cP))]

    #Tableau d'affectation pour le i-eme étudiant
    affectation={} 

    #Initialisation de la Queue 
    q = queue.Queue(len(list_etu))
    for etu in list_etu:
        q.put((int)(etu))

    #Initialisation du tableau de suivi
    suivi=[0 for i in range (len(list_etu))]
    
    while(not q.empty()):
        etu_courant=q.get()
        while(len(cE[etu_courant])!=0):
            
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

    return affectation


def GS_master(cE,cP,capacity):
    """
    Tant qu'il existe un Master libre qui n'a pas proposer a tout les étudiants, il choisis le premier étudiant E
    dans sa liste, si le master n'a pas atteint sa capacite max et que l'étudiant est dans aucun master 
    alors on prend l'etudiant E. Sinon on doit comparer si l'etudiant prefere sont master actuelle ou le master qui propose.
    Si il prefere le master courant on remplace le pire master de l'étudiant par le master courant. Sinon E reste dans son master
    """

    #Initialisation list_master
    list_master=[i for i in range(len(cP))]
    
    #Initialisation matrice des preferences des etudiants pour chaque master
    tabPref=deepcopy(cE)
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
    
    while(not q.empty()):
        
        master_courant=q.get()
        is_in.remove(master_courant)

        while((int)(capacity[master_courant])>0 and suivi[master_courant]<len(cP[master_courant])):

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
    
    return affectation


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
    dix_tests_master = []
    dix_tests_etu = []
    
    for n in range(200,2200,200):
        cE = generate_cE(n,9)
        cP = generate_cP(n,9)
        print("n = ",n)
        capacites = [random.randint(1, n//2) for _ in range(9)] # capacites entre 1 et n/2 pour equité
        while sum(capacites) != n:
            diff = n-sum(capacites)
            if diff > 0: # on met diff dans une capacite random
                capacites[random.randint(0, 8)] += diff
            if diff < 0: #si sum(capacites) > n
                # on ajt diff(negatif) à une capacite random
                ind = random.randint(0, 8)
                capacites[ind] = max(1, capacites[ind] + diff) # max entre 1 pourr eviter des capacités negatives

        capacites2=deepcopy(capacites) # car les fonctions GS modifient directement le tableau initial  
        debut = time.time()
        affectes_master = GS_master(cE,cP, capacites)
        fin = time.time()
        print("coté master : ", fin-debut)
        dix_tests_master.append(fin-debut)
        debut = time.time()
        affectes_etu = GS_etu(cE,cP, capacites2)
        fin = time.time()
        dix_tests_etu.append(fin-debut)
        print("coté etu : ", fin-debut)

    print("\n")
    print("moyenne temps parcours = ", sum(dix_tests_master) / len(dix_tests_master)," secondes")
    print("moyenne temps etu = ", sum(dix_tests_etu) / len(dix_tests_etu)," secondes")
    

    val_n=[n  for n in range(200,2200,200)]
    plt.figure(figsize=(8,5))

    plt.plot(val_n,dix_tests_etu,label="Temps_etu",color="blue")
    plt.plot(val_n,dix_tests_master,label="Temps_master",color="red")
    plt.xlabel("n")
    plt.ylabel("Temps d'execution (s)")
    plt.title("Graphique des temps d'executions de Gale-Shapley")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()
    return
    

def PLNE(k, prefetu, prefspe):
    """
    Variable : Xij = 1 si l'etudiant i est affecté au parcours j, 0 sinon
    Fonction objective : max
    """
    # #tableau des utilités cote etudiant et cote master
    # util_etu = [-1 for i in range(len(prefetu)) for j in range(len(prefspe))]
    # util_spe = [-1 for i in range(len(prefspe)) for j in range(len(prefetu))]

    # for i in range(len(prefetu)):
    #     for j in prefetu[i]:
    #         util_etu[prefetu[i]][prefetu[i][j]] = len(prefetu[i])-j #rang du parcours j pour l'etudiant i
    #         util_spe[prefspe[j]][prefspe[j][i]] = len(prefspe[j])-i #rang de l'etudiant i pour le parcours j

    # #tableau des sommes des utilités
    # sum_util = [-1 for i in range(len(prefspe)) for j in range(len(prefetu))]

    # for i in range(len(util_etu)):
    #     for j in range(len(util_etu[i])):
    #         sum_util[i][j] = util_etu[i][j] + util_spe[j][i]

    

    prefetu_k = [prefetu[i][j] for i in range(len(prefetu)) for j in range(k)]
    prefspe_k = [prefspe[i][j] for i in range(len(prefspe)) for j in range(k)]
    GS_etu(prefetu_k, prefspe_k,capacity_master("PrefSpe.txt"))

    return