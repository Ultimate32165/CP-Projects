n = int(input())
a = 0
while (n > 0):
    m = map(int, input().split())
    l = list(m)
    if sum(l) >= 2:
        a += 1
    n -= 1

print(a)
