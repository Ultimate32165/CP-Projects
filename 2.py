n = int(input())
a = []
if n>=1 or n<=100:
  for i in range(n):
    b = input()
    if len(b)<1 or len(b)>100:
      print("Invalid Try Again")
      b = input()

    if len(b)>10:
      b = b[0]+str(len(b)-2)+b[-1]
      a.append(b)
    else:
      a.append(b)


  print(n)
  for item in a:
    print(item)
else:
  print("Invalid Number")
  n = int(input())
