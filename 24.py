t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())

    while True:
        # Gellyfish's turn (odd turn)
        if b > d:
            d -= 1
        else:
            b -= 1

        if b <= 0 or d <= 0:
            print("Gellyfish")
            break

        # Tricolor Pansy's turn (even turn)
        if a > c:
            c -= 1
        else:
            a -= 1

        if a <= 0 or c <= 0:
            print("Flower")
            break
