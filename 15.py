n = int(input())
if n>=1 and n<=50:
  b = input()
  removed = 0
  c = list(b)
  for i in range(len(c)-1):
    if c[i]==c[i+1]:
      if c[i+1] not in c:
        break
      removed +=1

  print(removed)