n = int(input())
current_passengers = 0
max_capacity_needed = 0

for i in range(1,n+1):
  a,b = map(int,input().split())
  current_passengers = current_passengers-a
  current_passengers = current_passengers+b
  if current_passengers>max_capacity_needed:
    max_capacity_needed = current_passengers

print(max_capacity_needed)