#include <stdio.h>
#include <string.h>
int is_luck(int count){
  char s[20];
  sprintf(s,"%d",count);
  for (int i = 0; i < strlen(s); i++)
  {
    if (s[i]!='4' && s[i]!='7'){
      return 0;
    }
  }
  return 1;
}



int main(){
  char n[1000];
  scanf("%s",n);
  int count=0;
  for (int i = 0; i < strlen(n); i++)
  {
    if (n[i]=='4' || n[i]=='7'){
      count++;
    }
  }
  int m = is_luck(count);
  if (m){
    printf("YES\n");
    
  }
  else{
    printf("NO\n");
    
  }
  return 0;
}