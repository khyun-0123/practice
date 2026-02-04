n = int(input())
scholar_list = []
year_list = []


for _ in range(n):
    a, b = input().split()

    scholar_list.append(a)
    year_list.append(b)

iphak = max(year_list)

for x in range(n):
    if year_list[x] == iphak:
        print(scholar_list[x])
        break