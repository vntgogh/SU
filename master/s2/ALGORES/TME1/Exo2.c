#include <stdio.h>
#include <string.h>
#include <mpi.h>
#define BUFLEN 20

int main(int argc, char *argv[]){
    int rank;
    int nombre;
    
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &nombre);
    printf("Processus %d sur %d : Hello MPI\n", rank, nombre);
    MPI_Finalize();
    return 0;
}