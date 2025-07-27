import string
n = int(input())
a = input()
b = a.lower()
alphabet = list(string.ascii_lowercase)
if len(a)==n:
  condition = 1
  for i in alphabet:
    if i not in b:
      condition = 0
  if condition:
    print("YES")
  else:
    print("NO")
  
