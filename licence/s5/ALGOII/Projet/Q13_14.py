import math
import random
import Algo2_v3 as A2
import Algo3 as A3


def TGC(k,V):
    S=0
    j=1
    #print(k)
    if k>=3:
        for S in range(V[3]+2,V[k-1]+V[k]-1):
            for j in range(k):
                if(V[j]<S) and (A3.AlgoGlouton2(S,k,V)>1+A3.AlgoGlouton2(S-V[j],k,V)):
                    return False
    return True


"""sc_random(k,pmax) - retourne un systeme de capacite de taille k avec des élement aléatoire de 2 a pmaxz"""
def sc_random(k,pmax):
    V=[0 for _ in range(k)]
    rtab=[0 for _ in range(k-1)]
    V[0]=1
    for i in range(k-1):
        var=random.randint(2,pmax)
        while(rtab.__contains__(var)):
            var=random.randint(2,pmax)
        rtab[i]=var
    rtab.sort()
    for i in range(1,k,1):
        V[i]=rtab[i-1]
    return V

"""proportion_GloutonCompatible(k,pmax) - retourne la proportionnalité de systeme glouton compatible de taille 3 a k si k!=1,2"""
def proportion_GloutonCompatible(k,pmax):
    nb_GC=0
    if(k==1 or k==2):
        return 100
    else:
        for i in range(3,k):
            is_glouton=TGC(i-1,sc_random(i,pmax))
            print(k,i,is_glouton)
            if(is_glouton):
                nb_GC+=1
    return ((nb_GC/k)*100)


"""resolution (f,pmax) - ecris dans un fichier les pires écart et les moyens pour la solution des algo II et III pour un même systeme, 
                        un S qui varie de pmax a f*pmax,

"""


def resolution(f,pmax):
    nb_GC=0
    nb_NGC=0
    with open("eval_glouton_compatible.txt","w") as fichier:
        fichier.write("f = "+(str)(f)+"\npmax = "+(str)(pmax)+"\n")
        fichier.write("V Pire_Ecart Ecart_Moyen\n")

    for i in range(10,50,10):
        pire_ecart=0
        ecart_moyen=0
        nb_ecart=0
        V=sc_random(i*2,pmax)
        print(V)
        if(TGC(i,V),pmax):
            #print("glouton compatible")
            nb_GC+=1
        else:
            #print("non compatible")
            nb_NGC+=1
            for j in range(pmax,pmax*f,1):
                res_A2=A2.backward2(j,i,V)
                res_A3=A3.AlgoGlouton2(j,i,V)
                print(res_A2,res_A3)
                if(abs(res_A2-res_A3)>=pire_ecart):
                    pire_ecart=abs(res_A2-res_A3)
                ecart_moyen+=abs(res_A2-res_A3)
                nb_ecart+=1
            with open("eval_glouton_compatible.txt","a") as fichier:
                fichier.write("Systeme non glouton compatible : "+(str)(i)+"\n")
                fichier.write("[")
                fichier.writelines(f"{v}," for v in V)
                fichier.write("]\n")
                fichier.write("Pire ecart = "+(str)(pire_ecart)+"\n")
                fichier.write("Ecart Moyen = "+(str)(ecart_moyen/nb_ecart)+"\n")


"""eval_multiple_proportion(Q,pmax) - ecris dans un fichier des proportions de systeme glouton compatible allant jusqu'a Q"""

def eval_multiple_proportion(Q,pmax):
    with open("eval_"+(str)(Q)+"_glouton_proportion.txt", "w") as fichier:
        fichier.write("K proportionalite\n")

    for k in range (1,Q+1,1):
        #print(k)
        prop=proportion_GloutonCompatible(k,pmax)
        with open("eval_"+(str)(Q)+"_glouton_proportion.txt", "a") as fichier:
            fichier.write((str)(k)+" "+(str)(prop)+"\n")
    
#resolution(2,89)
eval_multiple_proportion(30,31)


    