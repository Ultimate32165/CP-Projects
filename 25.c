#include <stdio.h>

int main(){
  int n;
  scanf("%d",&n);
  int arr[101];
  int p=0;
  for (int i = 0; i < n; i++)
    {
      scanf("%d",&arr[i]);
    }
    
  for (int i = 0; i < n; i++)
  {
    if(arr[i]==1){
      p=1;
    }
  }
  if(p){
    printf("HARD\n");
    
  }
  else{
    printf("EASY\n");
    
  }
  return 0;
}