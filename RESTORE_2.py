# cook your dish here
def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True
def primeList(size):
    retList=list()
    num=2
    while(size>0):
        if(isPrime(num)):
            retList.append(num)
            size-=1
        num+=1
    return retList
# --------------------------------------------------------
for t in range(int(input())):
    size = int(input())
    B = input().split()
    for i in range(0,len(B)):
        B[i]=int(B[i])
    A=primeList(len(B))
    idx=list()
    for i in range(1,len(B)+1):
        idx.append(i)
    for i in range(0,len(B)):
        if(idx[i]!=B[i]):
            A[i]=A[B[i]-1]
    for i in range(0,size):
        if(i==size-1):
            print(A[i])
        else:
            print(A[i],end=" ")
        