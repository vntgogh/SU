#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

#define TAGINIT    0
#define NB_SITE 6

void simulateur(void) {
   int i;

   /* nb_voisins[i] est le nombre de voisins du site i */
   int nb_voisins[NB_SITE+1] = {-1, 3, 3, 2, 3, 5, 2};
   int min_local[NB_SITE+1] = {-1, 12, 11, 8, 14, 5, 17};

   /* liste des voisins */
   int voisins[NB_SITE+1][5] = {{-1, -1, -1, -1, -1},
            {2, 5, 3, -1, -1}, {4, 1, 5, -1, -1}, 
            {1, 5, -1, -1, -1}, {6, 2, 5, -1, -1},
            {1, 2, 6, 4, 3}, {4, 5, -1, -1, -1}};
                               
   for(i=1; i<=NB_SITE; i++){
      MPI_Send(&nb_voisins[i], 1, MPI_INT, i, TAGINIT, MPI_COMM_WORLD);    
      MPI_Send(voisins[i], nb_voisins[i], MPI_INT, i, TAGINIT, MPI_COMM_WORLD);    
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

   int pere = -1;
   int receive[nv];
   for (int y=0; y<nv;y++){
      receive[y] = 0;
   }

   if (rang == 1){
      pere = -1;
      for (int i = 0; i < nv; i++){
         printf("Le noeud %d envoie à %d\n", rang, voisin[i]);
         MPI_Send(&local, 1, MPI_INT, voisin[i], TAGINIT, MPI_COMM_WORLD);
      }
      for (int a = 0; a <nv; a++){
         int resultat;
         MPI_Recv(&resultat, 1, MPI_INT, MPI_ANY_SOURCE, TAGINIT, MPI_COMM_WORLD, &status);
         printf("Le noeud %d reçoit la val de %d\n", rang, status.MPI_SOURCE);
         if (local > resultat){
            local = resultat;
         }
      }
   }
   else{
      for (int b = 0; b <nv; b++){
         int resultat;
         MPI_Recv(&resultat, 1, MPI_INT, MPI_ANY_SOURCE, TAGINIT, MPI_COMM_WORLD, &status);
         if (local > resultat){
            local = resultat;
         }
         printf("Le noeud %d reçoit message de %d\n",rang, status.MPI_SOURCE);

         if (pere == -1){
            pere = status.MPI_SOURCE;
            for (int c = 0; c < nv; c++){
               if (voisin[c] != status.MPI_SOURCE){
                  printf("Le noeud %d envoie à %d\n", rang, voisin[c]);
                  MPI_Send(&local, 1, MPI_INT, voisin[c], TAGINIT, MPI_COMM_WORLD);
               }
            }            
         }
         receive[g] = 1;
      
      }
      printf("Le noeud %d à reçu tout les messages, envoie à pere %d\n", rang, voisin[pere]);
      MPI_Send(&local, 1, MPI_INT, voisin[pere], TAGINIT, MPI_COMM_WORLD);
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