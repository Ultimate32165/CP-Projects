#include <stdio.h>
#include <string.h>

int main(){
    char word[100];
    scanf("%s", word);
    
    int up = 0;
    int low = 0;    
    for (int i = 0; i < strlen(word); i++)
    {

        if(word[i] >= 'A' && word[i] <= 'Z'){
            up += 1;
        }
        else if(word[i] >= 'a' && word[i] <= 'z'){
            low += 1;
        }
    }
    

    if (up > low){
        for (int i = 0; i < strlen(word); i++)
        {
            if (word[i] >= 'a' && word[i] <= 'z'){
                word[i] -= 32; 
            }
        }
    }
    else{
        for (int i = 0; i < strlen(word); i++)
        {
            if (word[i] >= 'A' && word[i] <= 'Z'){
                word[i] += 32;
            }
        }
    }
    
    printf("%s", word);
    return 0;
}