t = int(input())

def dodo(n):
  for i in range(100):
    for j in range(100):
      if (i+j)**2==n:
        return f"{i} {j}"
  return 0

while (t>0):
  n = int(input())
  result = dodo(n)
  if result:
    print(result)
  else:
    print(-1)
  t-=1