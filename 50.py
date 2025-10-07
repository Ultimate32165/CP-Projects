n, k, l, c, d, p, nl, np = map(int, input().split())

drink = k*l
toast = drink/nl
toast2 = c*d
toast3 = p/np
answer = min(toast, toast2, toast3)/n
print(int(answer))
