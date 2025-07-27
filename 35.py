a = str(input())
b = str(input())
c = []
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] == b[i]:
            c.append("0")
        else:
            c.append("1")

print("".join(c))
