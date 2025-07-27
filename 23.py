n, h = map(int, input().split())
l = list(map(int, input().split()))
width = 0
for i in l:
    if i <= h:
        width += 1
    if i > h:
        width += 2

print(width)
