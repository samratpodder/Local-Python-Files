import math
def isPrime(n): 
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True
def primeList(size):
    primes=list()
    num=2
    while(size>0):
        if(isPrime(num)):
            primes.append(num)
            size-=1
        num+=1
    return primes
# --------------------------------------------------------
for t in range(int(input())):
    size = int(input())
    B = input().split()
    for i in range(0,len(B)):
        B[i]=int(B[i])
    A=primeList(len(B))
    for i in range(0,len(B)):
        j=B[i]
        j=j-1
        while(A[j]%A[i]!=0):
            if(A[i]<=A[j]):
                A[i]+=1
            if(A[i]>A[j]):
                A[i]-=1
    # print("%f seconds",(time.process_time()-starttime))
    for i in range(0,size):
        if(i==size-1):
            print(A[i])
        else:
            print(A[i],end=" ")