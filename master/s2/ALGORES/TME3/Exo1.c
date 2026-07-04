#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TAGINIT    0
#define TAGELEC    1
#define NB_SITE 6

void simulateur(void) {
   int i;

   /* nb_voisins[i] est le nombre de voisins du site i */
   int nb_voisins[NB_SITE+1] = {-1, 2, 3, 2, 1, 1, 1};
   int min_local[NB_SITE+1] = {-1, 3, 11, 8, 14, 5, 17};

   /* liste des voisins */
   int voisins[NB_SITE+1][3] = {{-1, -1, -1},
         {2, 3, -1}, {1, 4, 5}, 
         {1, 6, -1}, {2, -1, -1},
         {2, -1, -1}, {3, -1, -1}};
                               
   for(i=1; i<=NB_SITE; i++){
      MPI_Send(&nb_voisins[i], 1, MPI_INT, i, TAGINIT, MPI_COMM_WORLD);    
      MPI_Send(voisins[i],nb_voisins[i], MPI_INT, i, TAGINIT, MPI_COMM_WORLD);
      MPI_Send(&min_local[i], 1, MPI_INT, i, TAGINIT, MPI_COMM_WORLD); 
   }
}

void calcul_min(int rang){
   MPI_Status status;
   int nv;
   MPI_Recv(&nv,1, MPI_INT, 0, TAGINIT, MPI_COMM_WORLD, &status);
   int voisin[nv];
   MPI_Recv(&voisin, nv, MPI_INT, 0, TAGINIT, MPI_COMM_WORLD, &status);
   int local;
   MPI_Recv(&local, 1, MPI_INT, 0, TAGINIT, MPI_COMM_WORLD, &status);

   int sent = false;
   int receive[nv];
   for (int y=0; y<nv;y++){
      receive[y] = 0;
   }

   for (int a = 0; a <nv-1; a++){
      int resultat;
      MPI_Recv(&resultat, 1, MPI_INT, MPI_ANY_SOURCE, TAGINIT, MPI_COMM_WORLD, &status);
      if (local > resultat){
         local = resultat;
      }
      for (int g = 0; g<nv; g++){
         if (voisin[g] == status.MPI_SOURCE){
            receive[g] = 1;
         }
      }
   }
   if (rang !=1){
      int num = 0;
      for (int z = 0; z<nv;z++){
         if (receive[z] == 0){
            if (!sent){
               MPI_Send(&local, 1, MPI_INT, voisin[z], TAGINIT, MPI_COMM_WORLD);
               sent = true;
               num = z;
            }
         }
      }
      MPI_Recv(&local, 1, MPI_INT, voisin[num], TAGELEC, MPI_COMM_WORLD,&status);
      receive[num] = 1;

      for (int d = 0; d<nv;d++){
         if (receive[d] != 0){
   
            MPI_Send(&local, 1, MPI_INT, voisin[d], TAGELEC, MPI_COMM_WORLD);
         }
      }
      
   }
   else{
      for (int b = 0; b<nv;b++){
         MPI_Send(&local, 1, MPI_INT, voisin[b], TAGELEC, MPI_COMM_WORLD);
      }
   }
   printf("Le noeud %d à pour val local : %d\n", rang, local);
   
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
// Question 2 : ? On a le même resultat en éxecutant plusieurs fois sur la meme machine, cependant on a pas pu tester sur des machines différent.