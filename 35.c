#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(){
  char a[100];
  char b[100];
  scanf("%s",a);
  scanf("%s",b);

  for (int i = 0; i <strlen(a) ; i++)
  {
    if(a[i]==b[i]){
      printf("0");
    }
    else{
      printf("1");
    }
      
  }
  
  return 0;
}