n=int(input())
l=list(map(int,input().split()))

b=w=l[0]
count=0

for s in l[1:]:
  if s>b:
    b=s
    count+=1
  if s<w:
    w=s
    count+=1
print(count)