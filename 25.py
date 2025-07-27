n = int(input())
p=0
if n>=1 and n<=100:
  opinions = list(map(int,input().split()))
  for i in opinions:
    if i==1:
      p=1
    
if p:
  print("Hard")
else:
  print("Easy")