#include <stdio.h>
#include <stdlib.h>

void gauss(float *a, float *b, int n){
    int i,j,k;
    float aux,aux2;
    for(i=0;i<n-1;i++){
        aux = *(a+i*n+i);
        for(k=i+1; k<n; k++){
            *(a + i*n + k) /= aux;
        }
        *(b+i) /= aux;
        for (k=i+1; k<n; k++){
            aux2 = *(a+ k*n +i);
            for (j=i+1; j<n; j++){
                *(a+ k*n +j) -= aux2* (*(a+ i*n +j));
            }
            *(b+k) -= aux2* (*(b+i));
        }
    }

    *(b+n-1) /= *(a+ n*n -1);
    for(i=n-2; i>=0; i--){
        aux = *(b+i);
        for (k=i+1; k<n; k++){
            aux -= *(a+i*n+k)* (*(b+k));
        }
        *(b+i)=aux;
    }
}

void gauss_sp(double* a, double *b, int n){
    int i, j, k;
    double aux, aux2;
    for (i = 0; i<n-1; i++){
        aux = *(a + i*n + i);
        for (k = i+1; k<n; k++){
            *(a + i*n + k) /= aux;
        }
        *(b + i) /= aux;
        for (k = i+1; k<n; k++){
            aux2 = *(a + k*n + i);
            for (j = i+1; j<n; j++){
                *(a + k*n + j) -= aux2 * *(a + i*n + j);
            }
            *(b + k) -= aux2 * *(b+i);
        }
    }
    *(b + n-1) /= *(a + n*n -1);
    for (i = n-2; i>=0; i--){
        aux = *(b + i);
        for (k = i+1; k<n; k++){
            aux -= *(a + i*n + k) * *(b +k);
        }
        *(b + i) = aux;
    }
}

int main(){
    float *a = malloc(sizeof(float)*4*4);
    float *b;
    char **c=malloc(sizeof(char*));
    int n=4;
    gauss(a,b,n);
    c[0]="Mélissa";
    c[1]="Adam";
    c[2]="Marion";
    c[3]="Thomas";

    float *p1, *p2;

    for(p1=a; p1<a+n; p1++, p2 ++, c++){
        printf("%s = %.2f * %.2f\n", *c, *(p1), *(p2));
    }
    float a,b,n=4;
    gauss_sp(&a,&b,n);
    
    free(a);
    return 0;
}