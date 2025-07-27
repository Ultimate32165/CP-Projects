#include <stdio.h>

int main(){
  int n;
  scanf("%d",&n);

  for (int i = 0; i < n; i++)
  {
    if (i%2==0){
      printf("I hate");
    }
    else if (i%2!=0){
      printf("I love");
    }
    if(i < (n-1)){
      printf(" that ");
    }
  }
  printf(" it");
  
  return 0;
}