n = int(input())
rooms = 0
for _ in range(n):
    p, q = map(int, input().split())
    if q-p >= 2:
        rooms += 1

print(rooms)
