#분해합 > 

n = int(input())
jarisu = int(len(str(n)))

min_num = max(1, n - (9 * jarisu))

for i in range(min_num, n):
    result = sum(map(int, str(i))) + i
    if result == n:
        print(i)
        break
else:
    print(0)