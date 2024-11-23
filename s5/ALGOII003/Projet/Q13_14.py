import math
import random
import backward as A2
import AlgoGlouton as A3


def TGC(k,V):
    S=0
    j=1
    if k>=3:
        for S in range(V[3]+2,V[k-1]+V[k]-1):
            for j in range(k):
                if(V[j]<S) and (A3.AlgoGlouton2(S,k,V)>1+A3.AlgoGlouton2(S-V[j],k,V)):
                    return False
    return True

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



#V[1] 0 pmax/k
#V[2] pmax/k * i -1 pmax/4 * i

def proportion_GloutonCompatible(k):
    nb_GC=0
    for i in range(1,k,1):
        if(TGC(i-1,sc_random(i,50))):
            nb_GC+=1
    return (nb_GC/k)*100



def resolution(f,pmax):
    nb_GC=0
    nb_NGC=0
    with open("eval_glouton_compatible.txt","w") as fichier:
        fichier.write("f = "+(str)(f)+"\npmax = "+(str)(pmax)+"\n")
        fichier.write("V Pire_Ecart Ecart_Moyen\n")

    for i in range(10,30,1):
        pire_ecart=0
        ecart_moyen=0
        nb_ecart=0
        V=sc_random(i*2,pmax)
        print(V)
        if(TGC(i,V)):
            print("glouton compatible")
            nb_GC+=1
        else:
            print("non compatible")
            nb_NGC+=1
            for j in range(pmax,pmax*f,1):
                res_A2=A2.backward2(j,i,V)
                res_A3=A3.AlgoGlouton2(j,i,V)
                #print(res_A2,res_A3)
                if(abs(res_A2-res_A3)>=pire_ecart):
                    pire_ecart=abs(res_A2-res_A3)
                ecart_moyen+=abs(res_A2-res_A3)
                nb_ecart+=1
            with open("eval_glouton_compatible.txt","a") as fichier:
                fichier.write("Systeme non glouton compatible : "+(str)(nb_NGC)+"\n")
                fichier.write("[")
                fichier.writelines(f"{v}," for v in V)
                fichier.write("]\n")
                fichier.write("Pire ecart = "+(str)(pire_ecart)+"\n")
                fichier.write("Ecart Moyen = "+(str)(ecart_moyen/nb_ecart)+"\n")

print(proportion_GloutonCompatible(51))