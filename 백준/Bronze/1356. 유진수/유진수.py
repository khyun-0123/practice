n = input()

for i in range(1,len(n)):
    ap = 1
    dui = 1

    for a in range(i):
        ap = ap*int(n[a])
    # print(ap)

    for b in range(i, len(n)):
        dui = dui*int(n[b])
    # print(dui)
        
    if ap==dui:
        print('YES')
        break
else:
    print('NO')