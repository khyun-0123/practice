n, m = map(int, input().split())

name_to_num = {}
num_to_name = {}

for i in range(1, n+1):
    temp = input().strip()
    name_to_num[temp] = i
    num_to_name[i] = temp

for _ in range(m):
    quest = input().strip()
    if quest.isdigit():
        print(num_to_name[int(quest)])
    else:
        print(name_to_num[quest])