from collections import Counter

def check(a,b,c):
  a = a.lower()
  b = b.lower()
  c = c.lower()

  normal = Counter(a+b)
  merged = Counter(c)

  return normal==merged

# Test
a= input()
b= input()
c=input()

if check(a,b,c):
  print("YES")
else:
  print("NO")

