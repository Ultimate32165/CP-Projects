#include <stdio.h>
#include <math.h>

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);

        int found = 0;

        for (int i = 0; i < 100 && !found; i++) {
            for (int j = 0; j < 100; j++) {
                if ((i + j) * (i + j) == n) {
                    printf("%d %d\n", i, j);
                    found = 1;
                    break;
                }
            }
        }

        if (!found) {
            printf("-1\n");
        }
    }

    return 0;
}
