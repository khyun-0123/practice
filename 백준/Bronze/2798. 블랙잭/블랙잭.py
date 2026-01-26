#블랙잭

n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse=True)

stop = 0

result = 0

for a in range(n-2):
    if stop == 1:
        break
    for b in range(a+1, n-1):
        if stop == 1:
            break
        for c in range(b+1, n):
            total = cards[a] + cards[b] + cards[c]
            if total > result and total <= m:
                result = total
            if result == m:
                stop = 1
                break

print(result)