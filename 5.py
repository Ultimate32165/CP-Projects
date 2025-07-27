n = int(input())
a = 0
while (n>0):
  b = input()
  if "++" in b:
    a+=1
  elif "--" in b:
    a-=1
  n-=1
print(a)