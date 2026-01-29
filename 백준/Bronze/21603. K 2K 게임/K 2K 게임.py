n, k = map(int, input().split())

answer_list = []
err = [k%10, (2*k)%10]

for i in range(1, n+1):
    if i in err:
        continue
    answer_list.append(i)

print(len(answer_list))
print(*(sorted(answer_list)))