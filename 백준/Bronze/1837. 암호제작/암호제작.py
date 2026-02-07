#문제 풀이 아이디어 > K 보다 작은 소수 구하고 그걸로 나누어떨어지면 안됨.
# ex) 2 ok, 2의 배수는 x (3도 마찬가지)
# 이렇게 쭉쭉 돌려서 루트 n까지 소수리스트 만들기

p, k = map(int, input().split())
root_k = int(k**0.5)+1

sosu_list = [True]*k
sosu_list[0] = sosu_list[1] = False

sosu_answ = []

for i in range(2, root_k):
    if sosu_list[i]==True:
        for j in range(i*i, k, i):
            sosu_list[j] = False

for i in range(2, k):
    if sosu_list[i] and p%i==0:
        print('BAD', i)
        break
else:
    print('GOOD')