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
    if(my_rank !=MASTER){
        sprintf(message, "Hello Master from %d", my_rank);
        dest = MASTER;
        MPI_Send(message, strlen(message)+1, MPI_CHAR,dest,tag,MPI_COMM_WORLD);

    }else{
        for(source=0;source < nb_proc;source++){
            if(source != my_rank){
                MPI_Recv(message, SIZE, MPI_CHAR, MPI_ANY_SOURCE, tag, MPI_COMM_WORLD, &status);
                printf("%s\n", message);
            }
        }
    }
    MPI_Finalize();
    return 0;
}


//* Question 1 : Chaque processus envoie un message au processus 0 (MASTER)
// Le message est Hello Master from <numéro_processus>
// Lorsqu'on est sur le processus 0, nous récupérons et nous affichons les messages envoyées par les autres processus */

/* Question 2 : Les messages des processus s'affiche dans l'ordre */

/* Question 3 : Les messages des processus s'affiche dans le désordre, car on récupère les messages en fonction de la FILE*/

