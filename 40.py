k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

k_list = [i for i in range(1, d+1) if i % k == 0]
l_list = [i for i in range(1, d+1) if i % l == 0]
m_list = [i for i in range(1, d+1) if i % m == 0]
n_list = [i for i in range(1, d+1) if i % n == 0]


j = set(k_list + l_list + m_list+n_list)
print(len(j))
