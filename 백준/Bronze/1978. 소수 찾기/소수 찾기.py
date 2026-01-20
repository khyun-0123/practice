## 소수 찾기
cnt = 0
n = int(input())

num_list = list(map(int, input().split()))

for i in num_list:
    if i == 1:
        continue
    for t in range(2, i):
        if i % t == 0:
            break
    else:
        cnt += 1

print(cnt)