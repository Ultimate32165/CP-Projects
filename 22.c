#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
  char word[101];
  char word2[101];
  char reversed_word[101];
  scanf("%s", word);
  scanf("%s",word2);
  int len = strlen(word);
  for (int i = 0; i < len; i++)
  {
    reversed_word[i] = word[len - 1 - i]; // Correct indexing
  }

  reversed_word[len] = '\0';

  if(strcmp(word2, reversed_word) == 0){
    printf("YES\n");
    
  }
  else{
    printf("NO\n");
    
  }
  return 0;
}