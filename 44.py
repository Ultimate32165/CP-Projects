n = int(input())
games = n*(n-1)
h=[]
a=[]
count=0
for i in range(n):
  c,d=map(int,input().split())
  h.append(c)
  a.append(d)
for i in range(n):
  for j in range(n):
    if h[i]==a[j]:
      count+=1

print(count)
