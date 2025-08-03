t = int(input())

for _ in range(t):
    n = input()
    l = []
    length = len(n)
    for i in range(length):
        digit = int(n[i])
        power = ((length-1)-i)
        place_value = digit * (10 ** power)
        if digit != 0:
            l.append(place_value)
    print(len(l))
    for items in l:
        print(items, end=" ")
    print()
