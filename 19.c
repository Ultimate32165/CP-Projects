#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char n[1000];
    int k;
    scanf("%s %d", n, &k);

    while (k--) {
        int len = strlen(n);
        if (n[len - 1] == '0') {
            n[len - 1] = '\0';  // Remove the last character
        } else {
            n[len - 1]--;       // Decrease the last digit
        }
    }

    printf("%s\n", n); 
    return 0;
}
