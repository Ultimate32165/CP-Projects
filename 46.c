#include <stdio.h>
#include <string.h>
int main(){
  int n;
  scanf("%d",&n);
  for (int i = 0; i < n; i++)
  {
    char arr[4];
    char ar1[4]="Yes";
    char ar2[4]="YeS";
    char ar3[4]="yes";
    char ar4[4]="YES";
    char ar5[4]="yES";
    char ar6[4]="yEs";
    char ar7[4]="yeS";
    char ar8[4]="YEs";
    scanf("%s",arr);
    if(strcmp(arr,ar1)==0 || strcmp(arr,ar2)==0 || strcmp(arr,ar3)==0 || strcmp(arr,ar4)==0 || strcmp(arr,ar5)==0 || strcmp(arr,ar6)==0 || strcmp(arr,ar7)==0 || strcmp(arr,ar8)==0){
      printf("YES\n");
    }
    else{
      printf("NO\n");
      
    }
  }
  
  return 0;
}