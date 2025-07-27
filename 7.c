#include <stdio.h>

int main(){
  int a[2];
  for (int i = 0; i < 2; i++)
  {
    scanf("%d",&a[i]);
    
  }
  printf("%d\n",(a[0]*a[1])/2);
  
  return 0;
}