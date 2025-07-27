#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(){
  char st1[100];
  char st2[100];
  scanf("%s",st1);
  scanf("%s",st2);
  for (int i = 0; st1[i] != '\0'; i++) {
        st1[i] = tolower(st1[i]);
    }
  for (int i = 0; st2[i] != '\0'; i++) {
        st2[i] = tolower(st2[i]);
    }
  printf("%d\n",strcmp(st1, st2));
  
  return 0;
}