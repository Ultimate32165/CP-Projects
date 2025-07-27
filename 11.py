a = input()
b = input()

if len(a) <= 100 and len(b) <= 100 and len(a) == len(b):
    c = a.lower()
    d = b.lower()

    if c == d:
        print(0)
    elif c > d:
        print(1)
    else:
        print(-1)
