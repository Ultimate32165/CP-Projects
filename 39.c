#include <stdio.h>

int main() {
    int n;
    char str[1001];
    int seen[26] = {0};
    int count = 0;

    scanf("%d", &n);
    scanf("%s", str);

    for (int i = 0; i < n; i++) {
        char ch = str[i];

        // Convert uppercase to lowercase manually
        if (ch >= 'A' && ch <= 'Z') {
            ch = ch + 32;
        }

        // Check if it's a lowercase letter
        if (ch >= 'a' && ch <= 'z') {
            int index = ch - 'a';
            if (seen[index] == 0) {
                seen[index] = 1;
                count++;
            }
        }
    }

    if (count == 26) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    return 0;
}
