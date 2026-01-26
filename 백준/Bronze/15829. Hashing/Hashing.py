#해시
MOD = 1234567891
alpha = 'abcdefghijklmnopqrstuvwxyz'

n = int(input())
hash_list = input().strip()
result = 0

for i in range(n):
    temp = alpha.find(hash_list[i])+1
    result = (result + (temp * (31 ** i)) % MOD) % MOD

print(result)