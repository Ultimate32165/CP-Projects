matrix = []
for i in range(5):
  row = list(map(int,input().split()))
  matrix.append(row)
  if 1 in row:
    one_row = i
    one_col = row.index(1)

moves = abs(one_row-2) + abs(one_col-2)
print(moves)