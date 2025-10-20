import math
t = int(input())

for i in range(t):
  a,b = map(int,input().split())
  g = 0
  if a<b:
    c = b-a
    g = math.ceil(c/10)
  elif a>b:
    c = a-b
    g = math.ceil(c/10)
  print(g)
  