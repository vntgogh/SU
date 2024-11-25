import Algo1 as A1
import Algo2_v3 as A2
import Algo3 as A3
import math
import time
import threading

S=1500
K=900
JUMP=100
START=1000


"""sc_expo(k,d,s) - Retourne un systeme de confiture expo V"""
def sc_expo(k,d,s):
    V=[(int)(d**i) for i in range (k)]
    #print(V)
    with open("data.txt","w") as fichier:
        fichier.write((str)(s)+"\n")
        fichier.write((str)(k)+"\n")
        for i in range(len(V)):
            fichier.write((str)(V[i])+"\n")
    return V

"""eval() - evalue le temps des algorithme pour une valeur k fixé allant jusqu'a la constante K,
            une valeur s allant jusqu'a S et enregistre pour chaque groupe d, ce temps.
"""
def eval():
    for k in range(100,K,100):
        with open("eval_temps_exec_"+(str)(k)+".txt", "w") as fichier:
            fichier.write("S k Algo1 Algo2 Algo3\n")
            fichier.write("\n#d2\n")
        algo1_60=False
        for s in range(START,S,JUMP):
            #Genere le systeme expo
            v=sc_expo(k,2,s)
            #Temps Algo 2
            debutalgo2=time.time()
            A2.backward(s,k,v)
            finalgo2=time.time()
            tempsalgo2=finalgo2-debutalgo2

            #Temps Algo 3
            debutalgo3=time.time()
            A3.AlgoGlouton(s,k,v)
            finalgo3=time.time()
            tempsalgo3=finalgo3-debutalgo3

            #Temps Algo 1
            if not algo1_60:
                stop_event=threading.Event()
                args = [s,v,stop_event]
                thread=threading.Thread(target=A1.main_threading,args=args)
                debutalgo1=time.time()
                thread.start()
                #On attend 60 seconde
                thread.join(timeout=60)
                finalgo1=time.time()
                if thread.is_alive():
                    print("Temps d'execution a 60")
                    stop_event.set()
                    tempsalgo1=60.0
                    algo1_60=True
                    thread.join()
                else:
                    tempsalgo1=finalgo1-debutalgo1
                    print("Temps d'execution < 60")
            else:
                tempsalgo1=60
            with open("eval_temps_exec_"+(str)(k)+".txt", "a") as fichier:
                fichier.write((str)(s)+" "+(str)(k)+" "+(str)((float)(tempsalgo1))+" "+(str)(tempsalgo2)+" "+(str)(tempsalgo3)+"\n")
        
        with open("eval_temps_exec_"+(str)(k)+".txt", "a") as fichier:
            fichier.write("\n#d3\n")
        algo1_60=False
        for s in range(START,S,JUMP):
            #Genere le systeme expo
            sc_expo(k,3,s)
            #Temps Algo 2
            debutalgo2=time.time()
            A2.backward(s,k,v)
            finalgo2=time.time()
            tempsalgo2=finalgo2-debutalgo2

            #Temps Algo 3
            debutalgo3=time.time()
            A3.AlgoGlouton(s,k,v)
            finalgo3=time.time()
            tempsalgo3=finalgo3-debutalgo3

            #Temps Algo 1
            if not algo1_60:
                stop_event=threading.Event()
                args = [s,v,stop_event]
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
                    algo1_60=True
                    thread.join()
                else:
                    tempsalgo1=finalgo1-debutalgo1
                    print("Temps d'execution < 60")
            else:
                tempsalgo1=60
            with open("eval_temps_exec_"+(str)(k)+".txt", "a") as fichier:
                fichier.write((str)(s)+" "+(str)(k)+" "+(str)((float)(tempsalgo1))+" "+(str)(tempsalgo2)+" "+(str)(tempsalgo3)+"\n")
        
        with open("eval_temps_exec_"+(str)(k)+".txt", "a") as fichier:
            fichier.write("\n#d4\n")
        algo1_60=False
        for s in range(START,S,JUMP):
            #Genere le systeme expo
            sc_expo(k,4,s)

            #Temps Algo 2
            debutalgo2=time.time()
            A2.backward(s,k,v)
            finalgo2=time.time()
            tempsalgo2=finalgo2-debutalgo2
            #Temps Algo 3
            debutalgo3=time.time()
            A3.AlgoGlouton(s,k,v)
            finalgo3=time.time()
            tempsalgo3=finalgo3-debutalgo3

            #Temps Algo 1
            if not algo1_60:
                stop_event=threading.Event()
                args = [s,v,stop_event]
                thread=threading.Thread(target=A1.main_threading,args=args)
                debutalgo1=time.time()
                thread.start()
                #On attend 60 seconde
                thread.join(timeout=60)
                finalgo1=time.time()
                if thread.is_alive():
                    #print("Temps d'execution a 60")
                    stop_event.set()
                    tempsalgo1=60
                    algo1_60=True
                    thread.join()
                else:
                    tempsalgo1=finalgo1-debutalgo1
                    #print("Temps d'execution < 60")
            else:
                tempsalgo1=60
            with open("eval_temps_exec_"+(str)(k)+".txt", "a") as fichier:
                fichier.write((str)(s)+" "+(str)(k)+" "+(str)((float)(tempsalgo1))+" "+(str)(tempsalgo2)+" "+(str)(tempsalgo3)+"\n")        

eval()



