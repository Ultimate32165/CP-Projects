bill = [100, 20, 10, 5, 1]
money = int(input())
total_bills = 0

for i in bill:
    count = money // i
    total_bills += count
    money %= i

print(f"Total bills used: {total_bills}")
