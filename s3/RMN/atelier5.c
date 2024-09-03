#include <stdio.h>

void gauss_jordan(float *a, float *b, int n) {
    for (int i = 0; i<n; i++) {
        float pivot = a[i*n + i];

        // Divise la ligne courante par le pivot
        for (int j = 0; j < n; j++) {
            a[i*n + j] /= pivot;
            b[i*n + j] /= pivot;
        }

        for(int k = 0; k < n; k++) {
            if (k!=i) {
                float f=a[k*n +i];
                for(int j=0; j<n; j++) {
                    a[k*n + j] -= f * a[i *n+j];
                    b[k*n + j] -= f * b[i*n + j];
                }
            }
        }
    }
}

int main(){
    // matrice de food
    float A[16] = {1, 2, 3.5, 2, 0.7, 1.2, 1.5, 1, 0.8, 1.1, 1.2, 0.8, 11, 15, 7, 5};

    // matrice de food pour chaque armée
    float B[16] = {82.4, 130.5, 149.9, 95.6, 43.1, 69.6, 81.5, 52, 74.1, 112.3, 102.8, 66.2, 166.5, 248.5, 228.5, 152};

    gauss_jordan(A, B, 4);  // 4=nombre de creatures

    // affichage de la matrice
    printf("Resultat :\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%.2f\t", B[i * 4 + j]);
        }
        printf("\n");
    }

    return 0;
}