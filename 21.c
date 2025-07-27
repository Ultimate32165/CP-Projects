#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
  int n;
  scanf("%d",&n);
  char* arr;
  arr =(char*)malloc(n*sizeof(char));
  scanf("%s",arr);
  int antonP=0,DanikP=0;
  for (int i = 0; i < n; i++)
  {
    if (arr[i]=='A'){
      antonP++;
    }
    else if(arr[i]=='D'){
      DanikP++;
    }
  }
  if (antonP>DanikP){
    printf("Anton\n");
    
  }
  else if(DanikP>antonP){
    printf("Danik\n");

    
  }
  else{
    printf("Friendship\n");
    
  }
  
  return 0;
}