#include <stdio.h>

int main(){
  int k,n,w;
  scanf("%d %d %d",&k,&n,&w);
  int money=0;

  if(k>=1 && w<=1000){
    for (int i = 1; i <= w; i++)
    {
      money = money + (i*k);
    }
    if (money<=n){

      printf("%d",0);
    }
    else{

      printf("%d",(money-n));
    }
  }
  return 0;
}