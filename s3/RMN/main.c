#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>
#include <stdbool.h>
#include <stdint.h>

int main(){

    //Exercice 1
    
    printf("Pour x = %d et y = %d, on a: C = %d\n", 1.41421356, 1.41427845, bitcommun(1.41421356, 1.41427845));
    printf("Pour x = %d et y = %d, on a: C = %d\n", 9.87452334, 9.87901342, bitcommun(9.87452334, 9.87901342));
    printf("Pour x = %d et y = %d, on a: C = %d\n", 10.07452334, 10.07901342, bitcommun(10.07452334, 10.07901342));
    printf("Pour x = %d et y = %d, on a: C = %d\n", 10.07452334, 10.07901342, bitcommun(-2.69998756, -2.70001234));
    
    

    return 1;
}