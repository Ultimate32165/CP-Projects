k, n, w = map(int, input().split())
money = 0
if k>=1 and w<=1000:
  for i in range(1, w+1):
      money = money+(i*k)
  if money<=n:
      print(0)
  else:
    print(money-n)
