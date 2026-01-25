n = int(input())

arr = list(input().strip())
arr_r = list(reversed(arr))

for i in range(n):
    if arr[i] == '?':
        arr[i] = arr_r[i]

for i in range(n):
    if arr[i] == '?':
        arr[i] = 'n'

print(*arr, sep='')