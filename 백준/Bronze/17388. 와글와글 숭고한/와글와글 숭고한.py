sung, go, han = map(int, input().split())

if sum([sung, go, han])>=100:
    print("OK")
else:
    minnum = min(sung, go, han)
    if minnum == sung:
        print('Soongsil')
    elif minnum == go:
        print('Korea')
    elif minnum == han:
        print('Hanyang')