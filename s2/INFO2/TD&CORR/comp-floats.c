#include <assert.h>

float surface_float(float lon, float lar){
  /* retourne la surface d'un rectangle de longueur lon et de largeur lar */
  return lon * lar;
}

float valeur_absolue(float x){
  /* retourne la valeur absolue d'un flottant*/
  if(x >= 0)
    return x;
  return -x;
}

int egal_eps(float x1, float x2, float eps){
  return valeur_absolue(x1 - x2) < eps;
}

int main(){
    assert(surface_float(0.2,0.3)==0.6);
  //assert(egal_eps(surface_float(0.1, 0.2), 0.02, 0.00001));
  // mauvais : assert(egal_eps(surface_float(0.1, 0.2), 0.02, 0.000000001));
  //assert(egal_eps(0.1 + 0.2 - 0.3, 0, 0.0000000000001));
  // mauvais  assert(egal_eps(0.1 + 0.2 - 0.3, 0, 0.000000000000001));
  return 0;
}
