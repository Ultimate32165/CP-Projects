n, k = map(str, input().split())
for _ in range(int(k)):
    if n[-1] == '0':
        n = n[:-1]
    elif n[-1] != '0':
        n = str(int(n[:])-1)

print(n)
