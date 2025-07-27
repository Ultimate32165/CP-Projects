import math

num = int(input())
l=[1,2,3,4,5]
k = [math.ceil(num/l[i]) for i in range(len(l))]
k = sorted(k)
print(k[0])