#include <stdio.h>
#include <string.h>
#include <mpi.h>
#include <stdlib.h>
#include <unistd.h>

#define MASTER 0
#define SIZE 128
#define ELEC 2
#define LEADER 99
int main(int argc, char **argv){
    int my_rank;
    int nb_proc;
    int source;
    int dest;
    int tag =0;

    int leader = -1;
    int msg;
    MPI_Status status;

    MPI_Init(&argc, &argv);
    srand(getpid());
    int initiateur = rand()%2;
    MPI_Comm_size(MPI_COMM_WORLD, &nb_proc);
    MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);
    
    if (initiateur){
        printf("%d est initiateur \n",my_rank);
        MPI_Send(&my_rank, 1, MPI_INT, (my_rank+1)%nb_proc,ELEC,MPI_COMM_WORLD);
    }

    while(1){
        MPI_Recv(&msg, SIZE, MPI_INT, (my_rank-1)%nb_proc, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
        
        if (status.MPI_TAG == ELEC){
            if (initiateur){

                if (msg > my_rank){
                    MPI_Send(&msg, 1, MPI_INT, (my_rank+1)%nb_proc,ELEC,MPI_COMM_WORLD);
                }
                else if (msg == my_rank){
                    MPI_Send(&msg, 1, MPI_INT, (my_rank+1)%nb_proc, LEADER,MPI_COMM_WORLD);
                }else{
                    printf("TOKEN DETRUIT %d\n", msg);
                }
            }
            else{
                MPI_Send(&msg, 1, MPI_INT, (my_rank+1)%nb_proc,ELEC,MPI_COMM_WORLD);
            }
        }
        else{
            leader = msg;
            printf("%d LEADER IS %d\n", my_rank, msg);
            MPI_Send(&msg, 1, MPI_INT, (my_rank+1)%nb_proc,LEADER,MPI_COMM_WORLD);
            break;
        }

    }

    

    MPI_Finalize();
    return 0;
}

/* Question 1 : Le processus avec l'identifiant le plus grand qui est initiateur dans le premier tour qui gagnera. Il le saura quand il recevra son propre id. */
