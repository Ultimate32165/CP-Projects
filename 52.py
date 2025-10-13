n = int(input())
l = list(map(int,input().split()))
police = 0
crime = 0
for i in l:
  if i>0 and i==1:
    police+=1
  elif i>1:
    police+=i
  else:
    if police>0:
      police-=1
    else:
      crime+=1
print(crime)