from datetime import datetime as dt

amount = int(input('How many digits do you want?(1 - 9999): '))
pain = True
left = 0
a = 0
n = 0

def check(l):
    if l % 6 == 0:
        a = 6
        n = l // 6
        pain = False
    elif l % 5 == 0:
        a = 5
        n = l // 5
        l = False
    elif l % 4 == 0:
        a = 4
        n = l // 4
        pain = False
    elif l % 3 == 0:
        a = 3
        n = l // 3
        pain = False
    elif l % 2 == 0:
        a = 2
        n = l // 2
        pain = False
    elif l == 1:
        a = 1
        n = 1
        pain = False
    else:
        a = 0
        n = 0
        pain = True
    return a, n, pain

for i in range(7):
    if amount % (10**i) == 0 and amount // (10**i) <= 6:
        if amount // (10**i) == 1:
            a = 5
            n = (10**(i-1)) * 2
        elif amount // (10**i) > 1 and amount // (10**i) <= 6:
            a = amount // (10**i)
            n = 10**i
        else:
            n = 10**i
            a = amount // (10**i)
            if a % 2 == 0:
                if (a // 2) <= 6:
                    n = n*2
                    a = a // 2
                else:
                    for i in range(10):
                        if (a % i) == 0 and (a // i) <= 6:
                            n = n * i
                            a = a // i
if a == 0:
    while pain:
        a, n, pain = check(amount)
        if pain == True:
            amount -= 1
            left = True

seed = int(str(dt.now().microsecond)[0:a])
num = ''
temp = 0
store = []

if a % 2 == 1:
    s1 = a//2
    s2 = s1 + 1
else:
    s1 = a//2
    s2 = s1

if a != 1:
    for i in range(n):
        temp = 0
        temp = seed**2
        seed = int(str(temp)[len(str(temp))//2 - s1: len(str(temp))//2 + s2])
        if len(str(seed)) != a:
            if seed != 0:
                seed = seed*dt.now().second + dt.now().minute
                seed = int(str(seed)[0:a])
            else:
                seed = (seed + dt.now().second) * dt.now().minute
                seed = int(str(seed)[0:a])
        elif seed == store:
            seed = int(str(temp)[0:a])
        elif seed == 960 or seed == 160:
            seed += dt.now().minute
        if seed in store:
            if i % 2 == 0:
                seed = seed*dt.now().minute + dt.now().second
            else:
                seed = seed + dt.now().minute*dt.now().second
            seed = int(str(seed)[0:a])
        num = num + str(seed)
        store.append(seed)
    if left:
        num = num + str(dt.now().microsecond)[(dt.now().minute * dt.now().second//(dt.now().hour + dt.now().year))%6]
else:
    num = str((dt.now().hour + ((dt.now().year)**(dt.now().day)))//(dt.now().minute * dt.now().second)%9)

print(num)
