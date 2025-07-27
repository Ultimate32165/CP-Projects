#include <stdio.h>

int main(){
  int n;
  scanf("%d",&n);
  int arr[100000];
  float frac=0;
  for (int i = 0; i < n; i++)
  {
    scanf("%d",&arr[i]);
    
  }
   for (int i = 0; i < n; i++)
  {
    frac = frac + arr[i];
    
  }
  float fraction = frac/n;

  printf("%f",fraction);
  return 0;
}