t = int(input())
for i in range(t):
  length = int(input())
  l = list(map(int,input().split()))
  n = len(l)
  if n==1:
    print("YES")
  else:
    l.sort()
    is_possible = True
    for i in range(n-1):
      if l[i+1] - l[i] > 1:
            is_possible = False
            break

    if is_possible:
        print ("YES")
    else:
        print ("NO")


