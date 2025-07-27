n = int(input())
l = list(map(int, input().split()))
p = l[1:]
m = list(map(int, input().split()))
q = m[1:]

b = set(p+q)

if len(b) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
