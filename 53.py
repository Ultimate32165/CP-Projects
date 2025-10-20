n = int(input())

for i in range(n):
  a,b,c,d = map(int,input().split())
  p = 0
  if a<b:
    p+=1
  if a<c:
    p+=1
  if a<d:
    p+=1
  print(p)