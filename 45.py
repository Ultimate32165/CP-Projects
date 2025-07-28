t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    lst = list(map(int, input().split()))
    coins = 0

    while lst:
        current = lst.pop(0)
        lst.sort()
        if current > c:
            coins += 1
        lst = [x * 2 for x in lst]
    print(coins)
