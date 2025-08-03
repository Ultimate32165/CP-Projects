#include <stdio.h>
#include <string.h>
#include <math.h>

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        char num[1001];
        scanf("%s", num);

        int length = strlen(num);
        int count = 0;
        int results[100];  // To store the place values

        for (int i = 0; i < length; i++) {
            int digit = num[i] - '0';
            if (digit != 0) {
                int power = length - 1 - i;
                results[count++] = digit * pow(10, power);
            }
        }

        printf("%d\n", count);
        for (int i = 0; i < count; i++) {
            printf("%d ", results[i]);
        }
        printf("\n");
    }

    return 0;
}
