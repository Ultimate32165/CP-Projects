a = []
num = int(input())
for i in range(num):
  j  = 1
  b = input()
  if b not in a:
      print("ok")
  else:
    print(f"{b}{j}")
    j+=1
  a.append(b)