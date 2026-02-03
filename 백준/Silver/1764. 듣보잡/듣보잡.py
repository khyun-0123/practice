#시간초과 > 리스트보다 set이 더 빠름(set은 해쉬 주소 활용)
n, m = map(int, input().split())
hear_list = set()
see_list = set()

for _ in range(n):
    hear_list.add(input())

for _ in range(m):
    see_list.add(input())

answ_list = list(hear_list & see_list)
answ_list.sort()

print(len(answ_list))
for x in answ_list:
    print(x)