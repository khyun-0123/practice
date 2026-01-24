a, b, c, d= map(int, input().split())

if a/b*c/d/2 == (a/b*c/d)//2:
    print("1")
else:
    print("0")