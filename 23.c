#include <stdio.h>
#include <string.h>
int main(){
  int n;
  int h;
  scanf("%d %d",&n,&h);
  int l[1001];
  int width=0;
  for (int i = 0; i < n; i++)
  {
    scanf("%d",&l[i]);   
  }
  for (int i = 0; i < n; i++)
  {
    if (l[i]<=h){
      width++;
    }
    else if(l[i]>h){
      width = width+2;
    }
  }
  printf("%d\n",width);
  
  
  return 0;
}