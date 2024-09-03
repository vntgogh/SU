// TME 2
#include <stdint.h>
#include <fenv.h>
#include <stdio.h>

void affiche(double x){
    double res=x;
    fesetround(FE_DOWNWARD); 
    printf("Arrondi à moins l'infini = %24.15e\n", res);
    fesetround(FE_UPWARD); 
    printf("Arrondi à plus l'infini = %24.15e\n", res);
    fesetround(FE_TONEAREST); 
    printf("Arrondi au plus près = %24.15e\n", res);
    fesetround(FE_TOWARDZERO); 
    printf("Arrondi vers 0 = %24.15e\n", res);

}
int main(){

    affiche(156.7);
    affiche(-7e-5);
    return 0;

}