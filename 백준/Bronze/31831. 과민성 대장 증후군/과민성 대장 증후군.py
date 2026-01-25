n, m = map(int, input().split())

day_list = list(map(int, input().split()))

current_stress = 0
cnt = 0

for x in day_list:
    current_stress += x

    if current_stress < 0:
        current_stress = 0

    if current_stress >= m:
        cnt += 1

print(cnt)