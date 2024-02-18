#include "poisson_series.h"
int main(void){
  SeriesTerm *term = malloc(sizeof(SeriesTerm));
  const int kmax = 3;
  const int Nmax = 3;
  const int k[6]  = {3,-2,-1,0,0,0};
  const int z[4]  = {0,0,0,1};
  for(int i=0;i<6;i++) term->k[i] = k[i];
  for(int i=0;i<4;i++) term->z[i] = z[i];
  term->coeff = 1. ;
  term->next = 0;
  const double l[2] = { 0 , 0.0};
  double complex expIl[2] , xy[4];
  for(int i=0;i<2;i++) expIl[i] = cos(l[i]) + I * sin(l[i]); 
  for(int i=0;i<4;i++) xy[i] = 0;
  xy[0] = 0.2;
  xy[1] = 0.1;
  double re,im;
  double dxy_re[4],dxy_im[4],dxybar_re[4],dxybar_im[4];
  double jac_re[64], jac_im[64];
  evaluate_series_and_jacobian(
		  expIl,xy,term,kmax,Nmax,&re,&im,
		  dxy_re,dxy_im,dxybar_re,dxybar_im,
		  jac_re,jac_im
		  );
  for(int i=0;i<8;i++){
	for(int j=0;j<8;j++){
	  if(i>j){
    	  	printf("%.5f + %.5f*i \t",jac_re[INDEX(i,j)],jac_im[INDEX(i,j)]);
	  }else{
    	  	printf("%.5f + %.5f*i \t",jac_re[INDEX(j,i)],jac_im[INDEX(i,j)]);
	  }
	}
	printf("\n");
  }
  int i=1; int j=4;
  printf("\n (%d,%d): %.5f + %.5f*i \n",i,j,jac_re[INDEX(i,j)],jac_im[INDEX(i,j)]);
  free(term);
return 0;
}
