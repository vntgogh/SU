#include <stdio.h>
#include <assert.h>

#define KMIN 2
#define KMAX 200

int sommeDiviseurs(int n){
  /* hypothese : n entier naturel
     retourne la somme des diviseurs stricts de n
   */
  int s = 1;
  for(int i=2; i <= n/2; i++)
    if(!(n%i))
      s += i;
  return s;
}

int k_parfait(int n, int k){
  /* hypothese : k, n entiers naturels
     retourne 1 si n est k-parfait, 0 sinon
  */
  return (k * n == sommeDiviseurs(n) + n);
}

int trouver_k_parfait(int n){
  /* hypothese : n entier naturel 

     retourne le plus petit k, KMIN <= k <= KMAX tq n est k parfait, ou -1 si un
     tel k n'existe pas
  */
  int sommeDiv = sommeDiviseurs(n) + n; // la somme des diviseurs large de n
  for(int k=KMIN; k <= KMAX; k++)
    if(sommeDiv == k * n)
      return k;
  return -1;
}

int main(){
  assert(trouver_k_parfait(6)==2);
  assert(trouver_k_parfait(120)==3);
  assert(trouver_k_parfait(20)==-1);
}
