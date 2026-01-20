#분해합 > 분해합이 최대가 되려면 각 자리 최대, 결국 999. 반대의 경우는 000.

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
