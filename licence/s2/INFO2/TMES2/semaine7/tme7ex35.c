#include <stdio.h>
#define NB_PLANETES 8

struct _planete{
    char nom[10];
    float densite;
    float distance;
    int satellite;
};
typedef struct _planete planete;

void afficheplanete(planete *p){
    printf("nom : %s, densite : %.2f, distance soleil : %.2f, nb satellites : %d\n", p->nom, p->densite, p->distance, p->satellite);
}

planete affichetoutesplanetes(planete *tab){
    for (int i=0;i<NB_PLANETES; i++){
        afficheplanete(tab+i);
    }return *tab;
}

void modifiedensite(planete *p, float nvd){
    p->densite = nvd;
}

int main(){
    planete systemeSolaire[NB_PLANETES] ={{"Mercure", 5.42, 58, 0},{"Venus", 5.25, 108.2, 0},{"Terre", 5.52,149.6,1},{"Mars",3.94,227.9,2},{"Jupiter",1.314,778.3,16},{"Saturne",0.69,1427,17},{"Uranus",1.19,2869,15},{"Neptune",1.6,4496,2}};
    affichetoutesplanetes(systemeSolaire);
    return 0;
}