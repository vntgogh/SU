/*Des chercheurs s'intéressent à la vitesse de propagation d'une épidémie dans une ville alors qu'un seul individu est initialement malade. 
Sachant qu'une seule personnne contamine x nouvelles personnes chaque jour, nous voulons savoir en combien de jours
 un certain pourcentage de la population de la ville sera contaminé. Pour simplifier les calculs, une personne contaminée le reste 
 et continue donc à contaminer d'autres personnes tous les jours suivant sa contamination.
Complétez la fonction jours qui prend en paramètre deux entiers, le nombre de personnes contaminées par une même personne chaque jour 
et la population totale de la ville (on suppose qu'un nombre entier est suffisant) ainsi qu'un réel, compris entre 0.0 et 100.0, 
correspondant au pourcentage de la population qui 'doit' être infecté. La fonction renvoie le nombre de jours au bout duquel le pourcentage, 
passé en paramètre, de la population de la ville est contaminé. N'oubliez pas qu'initialement une seule personne est contaminée.*/

#include <stdio.h>
#include <math.h>

int jours(int nbpjour, int poptot, float pct){
    int cpt = 0;
    float nbcontas = 1.0;
    while (nbcontas*100.0/poptot <pct){
        cpt++;
        nbcontas+= nbpjour*nbcontas;
    } return cpt;
}

/*Les chercheurs souhaitent maintenant savoir quel pourcentage de la population sera contaminé 
au bout d'un certain nombre de jours.
Complétez la fonction pourcentage qui prend trois entiers en paramètre, le nombre de personnes 
contaminées par une même personne chaque jour, la population totale de la ville et le nombre de 
jours étudiés. La fonction renvoie le pourcentage de la population contaminée au bout du nombre 
de jours donné.
Pour simplifier les calculs, nous faisons toujours l'hypothèse qu'une personne contaminée le 
reste et continue donc à contaminer d'autres personnes tous les jours suivant sa contamination.
Nous vous rappelons qu'initialement une seule personne est infectée.
Attention, on ne peut pas avoir plus de 100% de la population contaminée.*/

float pourcentage(int nbpjour, int poptot, int nbjour){
    float contas = 1.0;
    float pct = 1.0;
    int cpt = 0;
    while ( cpt < nbjour){
        cpt++;
        contas = contas + nbpjour*contas;
        pct += contas *100/poptot;
    }if (pct >=100.0){
        return 100.0;
    }
    return pct;
}

int main(){
    int j = jours(2, 10, 50.0);
    printf("%f pourcents de la population sera infecté en %d jours\n", 50.0,j);
    int pop=10000;
    int x=5;
    float pctg0 = 100.00;
    printf("pop=%d, vitesse=%d, pctg0=%.2f, nbjours=%d\n",pop,x,pctg0,jours(x,pop,pctg0));
    float pctg1 = 50.00;
    printf("pop=%d, vitesse=%d, pctg1=%.2f, nbjours=%d\n",pop,x,pctg1,jours(x,pop,pctg1));
    int jours = 2;
    printf("pop=%d, vitesse=%d, jours=%d, pourcentage=%.2f\n",pop,x,jours,pourcentage(x,pop,jours));
    int jourss = 3;
    printf("pop=%d, vitesse=%d, jours=%d, pourcentage=%.2f\n",pop,x,jourss,pourcentage(x,pop,jourss));
    int joursss = 6;
    printf("pop=%d, vitesse=%d, jours=%d, pourcentage=%.2f\n",pop,x,joursss,pourcentage(x,pop,joursss));
}