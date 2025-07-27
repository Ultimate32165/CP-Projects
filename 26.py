year = int(input())
year1 = year
while True:
  year1 = year1+1
  set_year = set(str(year1))
  if len(set_year) == 4:
    break

print(year1)