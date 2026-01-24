a, b = map(int, input().split())

deal = a-a*b*0.01

if deal < 100:
    print("1")
else:
    print("0")