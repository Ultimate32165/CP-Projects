#include <stdio.h>

int min(int x, int y) {
    return x < y ? x : y;
}

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        long long a, b, c, d;
        scanf("%lld %lld %lld %lld", &a, &b, &c, &d);

        long long min_cd = c < d ? c : d;
        long long remaining_c = c - min_cd;
        long long remaining_d = d - min_cd;

        if (b <= remaining_c)
            printf("Gellyfish\n");
        else
            printf("Flower\n");
    }

    return 0;
}
