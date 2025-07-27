t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total_ones = sum(a)
    has_consecutive_zeros = any(a[i] == 0 and a[i + 1] == 0 for i in range(n - 1))
    
    if total_ones > n - 1 or has_consecutive_zeros:
        print("YES")
    else:
        print("NO")
