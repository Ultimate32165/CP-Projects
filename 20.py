n = input()

lucky_count = 0
for digit in n:
    if digit == '4' or digit == '7':
        lucky_count += 1

# Now check if lucky_count itself is a lucky number
lucky_count_str = str(lucky_count)
allowed = {'4','7'}
is_lucky = all(d in allowed for d in lucky_count_str)


if is_lucky:
    print("YES")
else:
    print("NO")
