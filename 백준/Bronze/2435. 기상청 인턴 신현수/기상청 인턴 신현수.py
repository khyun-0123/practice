n, k = map(int, input().split())

num_list = list(map(int, input().split()))
asw_list = []

for i in range(0, len(num_list)-k+1):
    temp = 0
    for j in range(i, i+k):
        temp += num_list[j]
    asw_list.append(temp)

print(max(asw_list))