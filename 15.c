#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
  int n;
  char *arr;
  int removed=0;
  scanf("%d",&n);
  if(n<=50 && n>=1){    
    arr = (char*) malloc(n * sizeof(char));
  }
  scanf("%s",arr);
  for (int i = 0; i < n; i++)
  {
    if (arr[i]==arr[i+1]){
      removed++;
    }
     
  }
  printf("%d\n",removed);
  
  
  return 0;
}