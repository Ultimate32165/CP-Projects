#include <stdio.h>
#include <string.h>

int main() {
    int n;
    scanf("%d", &n);

    char curr[3], prev[3];
    int groups = 1;

    scanf("%s", prev);  // First magnet

    for (int i = 1; i < n; i++) {
        scanf("%s", curr);  // Next magnet
        if (strcmp(curr, prev) != 0) {
            groups++;
        }
        strcpy(prev, curr);  // Update for next comparison
    }

    printf("%d", groups);
    return 0;
}
