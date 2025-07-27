a = list(map(int,input().split("+")))
l = sorted(a)
for item in l[:-1]:
  print(f"{item}+",end="")
print(f"{l[-1]}")