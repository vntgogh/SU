#include <stdio.h>
#include <stdlib.H>

void decomp(float *a, int n){
    int i,j,k,il;
    float aux, aux2;
    float *L=a, *U=a;
    for (i=0;i<n-1;i++){
        aux= *(a+i*n+i);
        for (k=i+1; k<n; k++){
            *(a+i*n+k) /= aux;
        }
        for (k=i+1; k<n;k++){
            aux2= *(a+k*n+i);
            for (j=i+1;j<n;j++){
                *(a+k*n+j) -= aux2* *(a+i*n+j);
            }
        }
    }
    printf("L= \n");
    for (int i= 0; i <5; i++) {
        for (int j= 0; j <5; j++) {
            if(i> j){
                printf("%.2f\t", a[i*5+j]);
            }else if(i== j){
                printf("1.0\t");
            }else{
                printf("0.0\t");
            }
        }
        printf("\n");
    }
    printf("U= \n");
    for (int i= 0; i<5; i++) {
        for (int j= 0; j<5; j++) {
            if (i<= j) {
                printf("%.2f\t", a[i*5+j]);
            } else {
                printf("0.0\t");
            }
        }
        printf("\n");
    }
}

void invmat(float *a, int n){
    float aux;
    int i,j,k;
    for(i=0;i<n;i++){
        aux = *(a + n*i +i);
        for(j=0;j<n;j++){
            *(a + n*i + j) /= aux;
        }
        *(a + n*i +i) = 1.0/aux;
        for(k=0;k<n;k++){
            if (k!=i){
                aux = *(a +n*k + i);
                for(j=0;j<n;j++){
                    *(a +n*k + j) -= aux * (*(a +n*i + j));
                }
                *(a +n*k + i) = - aux* *(a +n*i + i);
            }
        }
    }
}


int main(){
    float A[9] = {2.0, 3.0,-1.0, 4.0, 4.0, -3.0, -2.0, 3.0, -1.0};

    /*invmat(A, 3);
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {

            printf("%.2f\t", A[i * 3 + j]);
        }
        printf("\n");
    }*/

    float B[25]={1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,1.0,-1.0,1.0,-1.0,1.0,1.0-2.0,4.0,-8.0,16.0,1.0,-3.0,9.0,-27.0,81.0};

    decompLU(B,5);
    return 0;

}