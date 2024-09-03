#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double somme(double n){
    if(n==0){
        return 1;
    }else{
        return n * somme(n-1);
    }
}

double sommef(double nb){
    if (nb==0){
        return 1;
    }else{
        return somme(nb)+sommef(nb-1);
    }
}

int main(){
    printf("%.0f\n", sommef(10));
    printf("%.0f\n", sommef(13));
    printf("%.0f\n", sommef(20));
    return 0;
}