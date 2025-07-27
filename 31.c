#include <stdio.h>

int main(){
  int n;
  int rooms=0;
  scanf("%d",&n);
  int p,q;
  for (int i = 0; i < n; i++)
  {
    scanf("%d %d",&p,&q);
    if(q-p>=2){
      rooms++;
    }
  }
  printf("%d\n",rooms);
  
  
  return 0;
}