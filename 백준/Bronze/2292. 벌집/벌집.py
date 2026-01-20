#벌집 > 공차가 등비인 계차수열의 형태. 일반항 만드려고 했는데 그건 불가능. 그냥 돌리면서 만나는지 체크. >인지 >=인지 체크 잘하기.
n = int(input())
num_list = []
temp = 1
i = 1

while True:
    temp = temp +6*(i-1)
    num_list.append(temp)
    if temp >= n:
        print(i)
        break
    i+=1