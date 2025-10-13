
n = int(input())
l = list(map(int, input().split()))
max_h = max(l)
i_max = -1

for i in range(n):
    if l[i] == max_h:
        i_max = i
        break
        
min_h = min(l)
i_min = -1 
for i in range(n - 1, -1, -1):
    if l[i] == min_h:
        i_min = i
        break

swaps_to_front = i_max
swaps_to_end = (n - 1) - i_min

total_swaps = swaps_to_front + swaps_to_end

if i_max > i_min:
    total_swaps -= 1

print(total_swaps)