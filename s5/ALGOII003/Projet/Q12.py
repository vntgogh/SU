import Algo1 as A1
import backward as A2
import AlgoGlouton as A3
import math
import time
import threading

S=1100
K=900
JUMP=100
START=100
def sc_expo(k,d,s):
    
    V = [(int)(d**i) for i in range(k)]  # Génère des capacités d^0, d^1, ..., d^(k-1)
    with open("data.txt", "w") as fichier:
        fichier.write((str)(s) + "\n")  # Écrit s puis k dans le fichier
        fichier.write((str)(k) + "\n")  
        for i in range(len(V)):
            fichier.write((str)(V[i]) + "\n")  # Écrit les capacités V[i]
    return V

#faire un fichier par k contenant un groupe de ligne pour d2 (d3,d4) avec les colonnes S k Algo1 Algo2 Algo3
def eval():
    s=S
    header_format = "{:<8}{:<8}{:<25}{:<25}{:<25}\n"
    row_format = "{:<8}{:<8}{:<25}{:<25}{:<25}\n"

    tempsalgo1=0
    tempsalgo2=0
    tempsalgo3=0
    
    for k in range(START,K,JUMP): # On fait varier k de START à K avec un pas JUMP
        with open("eval_temps_exec_"+(str)(k)+".txt", "w") as fichier:
            fichier.write(header_format.format("S", "k", "Algo1", "Algo2", "Algo3"))
            fichier.write("\n#d2\n") # Résultats pour d = 2
        for s in range(START,S,JUMP): # On fait varier s de START à S avec un pas JUMP
            sc_expo(k,2,s) # Génère le système de capacités Expo pour d = 2

            # Temps Algorithme II
            debutalgo2=time.time()
            A2.backward()
            finalgo2=time.time()
            tempsalgo2=finalgo2-debutalgo2

            # Temps Algorithme III
            debutalgo3=time.time()
            A3.AlgoGlouton()
            finalgo3=time.time()
            
            # Temps Algorithme I 
            stop_event=threading.Event()
            args = [stop_event]
            thread=threading.Thread(target=A1.main_threading,args=args)
            debutalgo1=time.time()
            thread.start()
            thread.join(timeout=60) #On attend 60 secondes

            finalgo1=time.time()
            if thread.is_alive():# Si le thread est encore actif après 60 secondes
                print("Temps d'execution a 60")
                stop_event.set() # Envoie un signal pour arrêter l'algorithme
                tempsalgo1=60 # Temps fixé à 60 seconde
                thread.join() # Attend la fin du thread
            else:# Si le thread termine avant 60s 
                tempsalgo1 = finalgo1 - debutalgo1 # Calcul du temps réel
                print("Temps d'execution < 60")

            # Écrit des résultats dans le fichier
            with open("eval_temps_exec_"+(str)(k)+".txt", "a") as fichier:
                    fichier.write(row_format.format(s, k, tempsalgo1, tempsalgo2, tempsalgo3))
        
        with open("eval_temps_exec_"+(str)(k)+".txt", "a") as fichier:
            fichier.write("\n#d3\n") # Résultats pour d = 3
        for s in range(START,S,JUMP):
            sc_expo(k,3,s)

            debutalgo2=time.time()
            A2.backward()
            finalgo2=time.time()
            tempsalgo2=finalgo2-debutalgo2

            debutalgo3=time.time()
            A3.AlgoGlouton()
            finalgo3=time.time()
            tempsalgo3=finalgo3-debutalgo3

            stop_event=threading.Event()
            args = [stop_event]
            thread=threading.Thread(target=A1.main_threading,args=args)
            debutalgo1=time.time()
            thread.start()
            #On attend 60 secondes
            thread.join(timeout=60)
            finalgo1=time.time()
            if thread.is_alive():
                print("Temps d'execution a 60")
                stop_event.set()
                tempsalgo1=60
                thread.join()
            else:
                tempsalgo1=finalgo1-debutalgo1
                print("Temps d'execution < 60")
            with open("eval_temps_exec_"+(str)(k)+".txt", "a") as fichier:
                    fichier.write(row_format.format(s, k, tempsalgo1, tempsalgo2, tempsalgo3))
        
        with open("eval_temps_exec_"+(str)(k)+".txt", "a") as fichier:
            fichier.write("\n#d4\n") # Résultats pour d = 4
        for s in range(START,S,JUMP):
            sc_expo(k,4,s)

            debutalgo2=time.time()
            A2.backward()
            finalgo2=time.time()
            tempsalgo2=finalgo2-debutalgo2

            debutalgo3=time.time()
            A3.AlgoGlouton()
            finalgo3=time.time()
            
            stop_event=threading.Event()
            args = [stop_event]
            thread=threading.Thread(target=A1.main_threading,args=args)
            debutalgo1=time.time()
            thread.start()
            #On attend 60 seconde
            thread.join(timeout=60)
            finalgo1=time.time()
            if thread.is_alive():
                print("Temps d'execution a 60")
                stop_event.set()
                tempsalgo1=60
                thread.join()
            else:
                tempsalgo1=finalgo1-debutalgo1
                print("Temps d'execution < 60")
            with open("eval_temps_exec_"+(str)(k)+".txt", "a") as fichier:
                    fichier.write(row_format.format(s, k, tempsalgo1, tempsalgo2, tempsalgo3))
        
eval()


