n = int(input())
num_list = []

for _ in range(n):
    num_list = list(map(int, input().split()))
    if 18 in num_list:
        if 17 in num_list:
            print(*num_list)
            print("both")
            print("")
        else:
            print(*num_list)
            print("mack")
            print("")
    elif 17 in num_list:
        print(*num_list)
        print("zack")
        print("")
    else:
        print(*num_list)
        print("none")
        print("")