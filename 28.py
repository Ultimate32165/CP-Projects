n = int(input())
l = []
for _ in range(n):
    a = int(input())
    l.append(a)

groups = 1  # At least one group always
for i in range(n - 1):
    if l[i] != l[i + 1]:
        groups += 1

print(groups)
