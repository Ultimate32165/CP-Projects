#include <stdio.h>
#include <stdlib.h>
int main(){
  int row[5][5];
  int one_row;
  int one_col;
  for (int i = 0; i < 5; i++)
  {
    for (int j = 0; j < 5; j++)
    {
      scanf("%d",&row[i][j]);    
      if(row[i][j]==1){
        one_row = i;
        one_col = j;
      }
    }
    
  }
  int moves;
  moves = abs(one_row-2) + abs(one_col-2);

  printf("%d\n",moves);
  
  
  
  
  return 0;
}