#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

#define TAGINIT    0
#define NB_SITE 6

#define DIAMETRE 5		/* !!!!! valeur a initialiser !!!!! */
#define DEG_IN_MAX 2
#define DEG_IN_OUT 2
void calcul_min(int rang) {
   MPI_Status status;
   int local;
   int msg;
   int nvo;
   int nvi;
   int vi[2];
   int vo[2];
   int SCount = 0;


   MPI_Recv (&nvi, 1, MPI_INT, 0, TAGINIT, MPI_COMM_WORLD, &status);
   MPI_Recv (&nvo, 1, MPI_INT, 0, TAGINIT, MPI_COMM_WORLD, &status);
   MPI_Recv (&vi, nvi, MPI_INT, 0, TAGINIT, MPI_COMM_WORLD, &status);
   MPI_Recv (&vo, nvo, MPI_INT, 0, TAGINIT, MPI_COMM_WORLD, &status);
   MPI_Recv (&local, 1, MPI_INT, 0, TAGINIT, MPI_COMM_WORLD, &status);
   int RCount[nvi];
   for (int y=0; y<nvi;y++){
      RCount[y] = 0;
   }
   for (int j=0; j< DIAMETRE; j++){
      int tout_recu = 1;
      while (tout_recu){
         for (int z=0;z < nvi;z++){
            if (RCount[z] >= SCount){
               tout_recu = 0;
            }
            else{
               tout_recu = 1;
            }
         }
      }
      for(int k = 0; k < nvo; k++){
         MPI_Send(&local, 1, MPI_INT, vo[k], TAGINIT, MPI_COMM_WORLD);
      }
      SCount++;
      for(int l = 0; l < nvi; l++){
         MPI_Recv(&msg, 1, MPI_INT, vi[l], TAGINIT, MPI_COMM_WORLD, &status);
         RCount[l] = RCount[l]+ 1;
         printf("Noeud %d : %d \n",rang,msg);
         if (msg < local){
            local = msg;
            printf("Changement local de %d : %d\n",rang, local);
         }
      }

   }
   printf("Le plus petit identifiant pour l'id %d est : %d\n", rang, local);
}
void simulateur(void) {
   int i;

   /* nb_voisins_in[i] est le nombre de voisins entrants du site i */
   /* nb_voisins_out[i] est le nombre de voisins sortants du site i */
   int nb_voisins_in[NB_SITE+1] = {-1, 2, 1, 1, 2, 1, 1};
   int nb_voisins_out[NB_SITE+1] = {-1, 2, 1, 1, 1, 2, 1};

   int min_local[NB_SITE+1] = {-1, 4, 7, 1, 6, 2, 9};

   /* liste des voisins entrants */
   int voisins_in[NB_SITE+1][2] = {{-1, -1},
				{4, 5}, {1, -1}, {1, -1},
				{3, 5}, {6, -1}, {2, -1}};
                               
   /* liste des voisins sortants */
   int voisins_out[NB_SITE+1][2] = {{-1, -1},
				{2, 3}, {6, -1}, {4, -1},
				{1, -1}, {1, 4}, {5,-1}};

   for(i=1; i<=NB_SITE; i++){
      MPI_Send(&nb_voisins_in[i], 1, MPI_INT, i, TAGINIT, MPI_COMM_WORLD);    
      MPI_Send(&nb_voisins_out[i], 1, MPI_INT, i, TAGINIT, MPI_COMM_WORLD);    
      MPI_Send(voisins_in[i], nb_voisins_in[i], MPI_INT, i, TAGINIT, MPI_COMM_WORLD);    
      MPI_Send(voisins_out[i], nb_voisins_out[i], MPI_INT, i, TAGINIT, MPI_COMM_WORLD);    
      MPI_Send(&min_local[i], 1, MPI_INT, i, TAGINIT, MPI_COMM_WORLD); 
   }
}

/******************************************************************************/

int main (int argc, char* argv[]) {
   int nb_proc,rang;
   MPI_Init(&argc, &argv);
   
   MPI_Comm_size(MPI_COMM_WORLD, &nb_proc);

   if (nb_proc != NB_SITE+1) {
      printf("Nombre de processus incorrect !\n");
      MPI_Finalize();
      exit(2);
   }
  
   MPI_Comm_rank(MPI_COMM_WORLD, &rang);
  
   if (rang == 0) {
      simulateur();
   } else {
      calcul_min(rang);
   }
   MPI_Finalize();
   return 0;
}