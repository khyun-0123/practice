while True:
    s = input().strip()
    if s == "0":
        break
    s_r = s[::-1]

    if s == s_r:
        print("yes")
    else:
        print("no")