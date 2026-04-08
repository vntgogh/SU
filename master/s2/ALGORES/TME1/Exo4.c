#include <stdio.h>
#include <string.h>
#include <mpi.h>
#define MASTER 0
#define SIZE 128

int main(int argc, char **argv){
    int my_rank;
    int nb_proc;
    int source;
    int dest;
    int tag =0;
    char message[SIZE];

    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &nb_proc);
    MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);

    if (my_rank == 0){
        MPI_Recv(message, SIZE, MPI_CHAR, (my_rank-1)%nb_proc, tag, MPI_COMM_WORLD, &status);
        printf("%d reçoit le message %s\n", my_rank, message);
        sprintf(message, "Hello mon successeur from %d", my_rank);
        dest = (my_rank+1)%nb_proc;
        MPI_Ssend(message, strlen(message)+1, MPI_CHAR,dest,tag,MPI_COMM_WORLD);
    }else{
        sprintf(message, "Hello mon successeur from %d", my_rank);
        dest = (my_rank+1)%nb_proc;
        MPI_Ssend(message, strlen(message)+1, MPI_CHAR,dest,tag,MPI_COMM_WORLD);
        MPI_Recv(message, SIZE, MPI_CHAR, (my_rank-1)%nb_proc, tag, MPI_COMM_WORLD, &status);
        printf("%d reçoit le message %s\n", my_rank, message);
    }

    MPI_Finalize();
    return 0;
}

/* Question 2 : Le programme ne se finit jamais parce que tous les processus commence par un MPI_Ssend. Or le MPI_Ssend attend que la dest fasse le MPI_Recv avant de continuer. C'est pourquoi on est bloqué. */

/* */