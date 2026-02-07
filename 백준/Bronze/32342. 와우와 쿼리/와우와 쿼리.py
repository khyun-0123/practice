n = int(input())
sound_list = []

for _ in range(n):
    temp = input()
    cnt=0
    for i in range(len(temp)-2):
        if temp[i]=='W' and temp[i+1]=='O' and temp[i+2]=='W':
            cnt+=1
    print(cnt)