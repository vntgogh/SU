#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <assert.h>
#include <math.h>
#define N 100000

void eval_Horner_1(double a, double *coeff_f, int n, double *f_a);
void eval_Horner_2(double a, double *coeff_f, int n, double *f_a, double *f_minus_a);
void mulpol(double *coeff_f, int n, double *coeff_g, int p, double * coeff_h, int *q);
void gauss_sp(double *a, double *b, int n);
void vandermonde(double *a, double *vander, int n);
void interpol_linalg(double *a, double *f_a, int n, double *coeff_f);
void interpol_Lagrange(double *a, double *f_a, int n, double *coeff_f);
void multpointeval_Horner1(double* coeff_f, double* a, int n, double *mulh1);
void multpointeval_Horner2(double* coeff_f, double* a, int n, double ** mulh2);
void multpointeval_linalg(double *a,double *coeff_f, int n, double *res);