def isPrime(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
    return False


t = int(input())
for i in range(t):
    s = input()
    z = 1
    a = 1
    w = []
    countk = 0
    countx = 0
    x = int(s.split(" ")[0])
    k = int(s.split(" ")[1])
    while (True):
        z = z + 1
        while (True):
            a = a + 1
            if z % a == 0:
                countx = countx + 1
                w.append(a)
            if (countx == x):
                break
        while (True):
            for g in w:
                if isPrime(g):
                    countk = countk + 1
    if (countk == k) & (countx == x):
        print(1)
        exit()
    print(0)
