a = input()
l = []
for i in a:
    l.append(i)
l[0] = l[0].capitalize()
p = "".join(l)
print(p)