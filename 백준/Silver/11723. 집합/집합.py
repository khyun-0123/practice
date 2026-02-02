import sys

s = set()

def f_add(num):
    s.add(num)

def f_remove(num):
    s.discard(num)

def f_check(num):
    if num in s:
        print(1)
    else:
        print(0)

def f_toggle(num):
    if num in s:
        s.remove(num)
    else:
        s.add(num)

def f_all():
    global s 
    s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
         13, 14, 15, 16, 17, 18, 19, 20}

def f_empty():
    global s
    s = set()

n = int(input())

for _ in range(n):
    cmd = sys.stdin.readline().strip()

    if cmd == 'all':
        f_all()
    elif cmd == 'empty':
        f_empty()
    else:
        cmd, num = cmd.split()
        num = int(num)
        if cmd == 'add':
            f_add(num)
        elif cmd == 'remove':
            f_remove(num)
        elif cmd == 'check':
            f_check(num)
        elif cmd == 'toggle':
            f_toggle(num)