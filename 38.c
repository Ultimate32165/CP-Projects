#include <stdio.h>

int main(){
  int n;
  scanf("%d",&n);
  for (int i = 0; i < n; i++)
  {
    int a,b;
    scanf("%d %d",&a,&b);
    if(a%b==0){
      printf("0\n");
    }
    else{
      int remainder = a%b;
      int moves = b-remainder;
      printf("%d\n",moves);
    }
  }
  
  return 0;
}