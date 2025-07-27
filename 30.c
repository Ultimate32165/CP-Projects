#include <stdio.h>

int main() {
    int n;
    long long func_; // Use long long to handle large inputs
    
    // Input n
    scanf("%d", &n);
    
    // Compute result based on parity
    if (n % 2 == 0) {
        func_ = n / 2;
    } else {
        func_ = -(n + 1) / 2;
    }
    
    // Print result
    printf("%lld\n", func_);
    
    return 0;
}