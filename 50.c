#include <stdio.h>
int min(int a,int b,int c){
  if(a<=c&&a<=b){
    return a;
  }
  else if(b<=c&&b<=a){
    return b;
  }
  else if(c<=a&&c<=b){
    return c;
  }
}
int main(){
  int n, k, l, c, d, p, nl, np;
  scanf("%d %d %d %d %d %d %d %d",&n, &k, &l, &c, &d, &p, &nl, &np);
  int drink = k*l;
  int toast = drink/nl;
  int toast2 = c*d;
  int toast3 = p/np;
  int answer = min(toast,toast2,toast3) / n;
  // printf("%d\n",toast);
  // printf("%d\n",toast2);
  // printf("%d\n",toast3);
  // printf("%d\n",min(toast,toast2,toast3));
  printf("%d\n",answer);
  return 0;
}